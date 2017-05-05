from FrameWork.Validation.Validate import Validate
from FrameWork.Users_And_Groups.ValidateUser import ValidateUser
from FrameWork.Roles_And_Authentication.ValidateRole import ValidateRoles
from Core.Verb.ValidateVerb import ValidateVerb
class ValidateEvent(Validate):

	def validateInput(self,request):
		try:
			del self.validationErrors[:]
		except :
			pass
		try:
			userid = request.data.get('user_id')
			noun = request.data.get('noun')
			verb =  request.data.get('verb')
			ValidateUser().validateInput(userid)
			ValidateRoles().validateNoun(userid, noun)
			ValidateVerb().validateInput(noun, verb)
		except Exception,e:
			self.validationErrors.append(e.__str__())

	def isvalid(self):
		if(len(self.validationErrors)>0):
			return False
		return True

	def getError(self):
		return self.getValidationErrors()
		