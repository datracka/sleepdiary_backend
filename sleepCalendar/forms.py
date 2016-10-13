from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Calendar


'''
This module is here just in case at some point we conclude that we might benefit from 
django's form validation system. For now, the data validation enforced through the models
is just fine. 
'''


class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password',)


class CalendarForm(ModelForm):
	class Meta:
		model = Calendar
		fields = ('sleepingQuality', 'tirednessFeeling')