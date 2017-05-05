from FrameWork.Validation.Validate import Validate
from FrameWork.Users_And_Groups import ValidateUser
from Core.Noun.ValidateNoun import ValidateNoun
from Core.Verb.models import Verb

class ValidateVerb(Validate):

	def validateInput(self,noun,verb):
		ValidateNoun().validateInput(noun)
		if(verb in ValidateNoun().allowedVerb(noun)):
			return True

		else :
			self.validationErrors.append("This verb is not allowed for this noun")
			