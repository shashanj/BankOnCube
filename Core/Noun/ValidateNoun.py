from FrameWork.Validation.Validate import Validate
from FrameWork.Users_And_Groups import ValidateUser
from Core.Noun.models import Noun

class ValidateNoun(Validate):

	def validateInput(self,noun):
		noun = Noun.objects.get(noun_code = noun)
		if(noun is None):
			self.validationErrors.append("no such noun Exist")

	def allowedVerb(self,noun):
		verbs = Noun.objects.get(noun_code = noun).allowedVerb.all()
		allowed = []
		for verb in verbs :
			allowed.append(verb.verb_code)

		return allowed