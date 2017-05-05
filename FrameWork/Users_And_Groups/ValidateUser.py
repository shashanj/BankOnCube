from FrameWork.Validation.Validate import Validate
from FrameWork.Users_And_Groups.UserSerializer import UserProfileSerializer,UserSerializer
class ValidateUser(Validate):

	def validateInput(self,user_id):
		user = UserProfileSerializer().get(user_id)
		if(user is None):
			self.validationErrors.append("no such user Exist")
		else:
			name = UserSerializer().get(user.usr.username)
			if(name is None):
				self.validationErrors.append("no such user Exist")
