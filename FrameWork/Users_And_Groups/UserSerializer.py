from rest_framework import serializers
from FrameWork.Users_And_Groups.models import UserProfile
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserProfile
		fields = '__all__'
		depth = 1

	def get(self,id) : 
		return UserProfile.objects.get(user_id = id)



class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		exclude = ('password',)
		depth = 1

	def get(self,username) : 
		return User.objects.get(username = username)