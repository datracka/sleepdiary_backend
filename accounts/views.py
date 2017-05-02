import jwt
import base64
from django.contrib.auth import authenticate, login
from authtools.models import User
from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token
from django.views.generic import View
from rest_framework.parsers import JSONParser
from requests import Response
from rest_framework.views import APIView
from rest_framework import status
import json
from rest_framework import viewsets, status, mixins, generics, permissions
from .jwtWrapper import jwtWrapper
from .validator import Validator
import accounts.constants as constant


class Sessions(APIView):
    http_method_names = ['post', 'get']
    permission_classes = (permissions.AllowAny,)
    parser_classes = (JSONParser,)

    def post(self, request):  # Create user new token (login in)

        messages = {'fields': {}, 'error': {}}

        # Server side fields validation
        rules = {
            'email': [constant.IS_REQUIRED, constant.IS_EMAIL],
            'password': [constant.IS_REQUIRED, constant.LENGTH_MIN_6]
        }

        validator = Validator()
        messages = validator.check(request, rules, messages)
        if len(messages['fields']) > 0:
            messages['error'] = constant.ERROR_FIELD_VALIDATION
            return JsonResponse(messages, status=status.HTTP_406_NOT_ACCEPTABLE)

        user = authenticate(email=request.data['email'], password=request.data['password'])

        if user is not None:
            if user.is_active:

                wrapper = jwtWrapper();
                encoded = wrapper.create(user.id)
                data = {
                    'token_key': str(encoded.decode("utf-8")),
                    'name': str(user.get_short_name()),
                    'userId': str(user.id)
                }
                return JsonResponse(data)
            else:
                messages['error'] = constant.ERROR_NOT_ACTIVE
                return JsonResponse(messages, status=status.HTTP_403_FORBIDDEN)
        else:
            messages['error'] = constant.ERROR_USER_NOT_FOUND
            return JsonResponse(messages, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, format=None):  # Delete user token (sign out)
        return 0;


class Users(APIView):
    http_method_names = ['post', 'get']
    permission_classes = (permissions.AllowAny,)
    parser_classes = (JSONParser,)

    def get(self, request):  # get user info - profile
        get_token(request)
        data = {}
        for key, value in dict(request.META).items():
            data[str(key)] = str(value)
        return JsonResponse(data)

    def post(self, request):

        messages = {'fields': {}, 'error': {}}

        print (dict(request.data).items())

        if len(dict(request.data).items()) == 0:
            messages['error'] = constant.ERROR_MISCELLANEOUS
            return JsonResponse(messages, status=status.HTTP_401_UNAUTHORIZED)

        rules= {
            'name': [constant.IS_REQUIRED],
            'email': [constant.IS_REQUIRED, constant.IS_EMAIL],
            'password': [constant.IS_REQUIRED, constant.LENGTH_MIN_6]
        }

        name = request.data['name']
        password = ''
        if 'password' in request.data:
            password = request.data['password']
        email = request.data['email']

        validator = Validator()
        messages = validator.check(request, rules, messages)

        if len(messages['fields']) > 0:
            messages['error'] = constant.ERROR_FIELD_VALIDATION
            return JsonResponse(messages, status=status.HTTP_406_NOT_ACCEPTABLE)

        # check if e-mail already exists
        if User.objects.filter(email=email).exists():
            messages['error'] = constant.ERROR_USER_ALREADY_EXISTS
            return JsonResponse(messages, status=status.HTTP_409_CONFLICT)

        # sign out new user
        new_user = User(name=name, email=email)
        new_user.set_password(password)
        try:
            new_user.save()
        except RuntimeError:
            messages['error'] = constant.ERROR_MISCELLANEOUS
            return JsonResponse(messages, status=status.HTTP_400_BAD_REQUEST)

        # login user automatically and return new JWT key
        wrapper = jwtWrapper();
        encoded = wrapper.create(new_user.id)
        data = {
            'token_key': str(encoded.decode("utf-8")),
            'name': str(new_user.get_short_name()),
            'userId': str(new_user.id)
        }

        return JsonResponse(data)

    def delete(self):
        return 0  # delete an existing user - profile

    def put(self):
        return 0  # modify an existng user - profile
