from rest_framework import serializers
from FrameWork.Roles_And_Authentication.models import Roles,UserRoles

class UserRolesSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserRoles
		fields = '__all__'
		depth = 1

	
	def getRoles(self,user_id):
		roles =  UserRoles.objects.filter(usersRole__user_id = user_id)[0].intendedRoles
		return roles.all()
