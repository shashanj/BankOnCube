from FrameWork.Validation.Validate import Validate
from FrameWork.Users_And_Groups import ValidateUser
from FrameWork.Roles_And_Authentication.models import Roles,UserRoles
from FrameWork.Roles_And_Authentication.UserRolesSerializer import UserRolesSerializer
from FrameWork.Roles_And_Authentication.RolesSerializer import RolesSerializer

class ValidateRoles(Validate):

	def validateInput(self,user_id,noun,verb):
		pass

	def validateRole(self,id,role) : 
		roles = UserRolesSerializer().getRoles(id)
		if(role in roles):
			return True
		self.validationErrors.append("this role is not valid for this user")
		

	def validateNoun(self,id,noun):
		roles = UserRolesSerializer().getRoles(id)
		rol = RolesSerializer()
		for role in roles :
			if(len(rol.getAllowedNoun(role)) > 0):
				return True

		self.validationErrors.append("this noun is not valid for this user")

		