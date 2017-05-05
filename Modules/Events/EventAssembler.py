from Core.Noun.models import *
from Core.Verb.models import *
from FrameWork.Users_And_Groups.models import *

class EventAssembler():

	def toPersistenObject(self,validated_data):
		validated_data['noun'] = Noun.objects.get(noun_code = validated_data.get('noun'))
		validated_data['user_id'] = UserProfile.objects.get(user_id =  validated_data.get('user_id'))
		validated_data['verb'] = Verb.objects.get(verb_code = validated_data.get('verb'))

		return validated_data