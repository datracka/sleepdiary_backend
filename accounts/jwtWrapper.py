import jwt
import time
from django.contrib.auth import authenticate
from requests import Response
from rest_framework import status


class jwtWrapper():
	# TODO: Move to a no reachable place!!
	secret = 'qwertyuiopasdfghjklzxcvbnm123456';

	def create(self, id):

		payload = {
			"iss": "Sleep Diary",
			"iat": time.time(),
			"aud": "www.sleepdiary.io",
			"sub": id,
			"Role": [
				"user",
			]
		}
		encoded = jwt.encode(
			payload,
			self.secret,
			algorithm='HS256'
		)

		return encoded

	def check(self, meta):
		parts = meta.split();

		if parts[0].lower() != 'bearer':
			return Response('Authorization header must start with Bearer', status=status.HTTP_401_UNAUTHORIZED)
		elif len(parts) == 1:
			return Response('Token not found', status=status.HTTP_401_UNAUTHORIZED)
		elif len(parts) > 2:
			return Response('Authorization header must be Bearer + \s + token', status=status.HTTP_401_UNAUTHORIZED)

		token = parts[1]

		try:
			payload = jwt.decode(
				token,
				self.secret,
				audience='www.sleepdiary.io'
			)
		except jwt.ExpiredSignature:
			return Response('token is expired', status=status.HTTP_401_UNAUTHORIZED)
		except jwt.InvalidAudienceError:
			return Response('incorrect audience, expected: YOUR_CLIENT_ID', status=status.HTTP_401_UNAUTHORIZED)
		except jwt.DecodeError:
			return Response('token signature is invalid', status=status.HTTP_401_UNAUTHORIZED)

		# if we get this point means token is verified
		return payload
