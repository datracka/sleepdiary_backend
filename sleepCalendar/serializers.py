from rest_framework import serializers
from .models import Day


# # Serializers define the API representation
# class UserSerializer(serializers.ModelSerializer):
# 	days = serializers.PrimaryKeyRelatedField(many=True, queryset=Day.objects.all())
#
# 	class Meta:
# 		model = User
# 		fields = ('id', 'username', 'email', 'days')

class DaySerializer(serializers.ModelSerializer):
	class Meta:
		model = Day
		fields = ('sleepingQuality', 'tirednessFeeling', 'date', 'uuid', 'user')
