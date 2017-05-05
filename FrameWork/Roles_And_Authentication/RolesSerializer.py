from rest_framework import serializers
from FrameWork.Roles_And_Authentication.models import Roles,UserRoles

class RolesSerializer(serializers.ModelSerializer):

	class Meta:
		model = Roles
		fields = '__all__'
		depth = 1

	
	def getAllowedNoun(self,role):
		return Roles.objects.get(roleCode = role).allowedNoun.all()
