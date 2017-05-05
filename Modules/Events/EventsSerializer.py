from rest_framework import serializers
from Modules.Events.models import Event
from Core.Noun.models import *
from Core.Verb.models import *
from FrameWork.Users_And_Groups.models import *
from Modules.Events.EventAssembler import  EventAssembler
class EventsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Event
		fields = '__all__'
		depth = 1

	def get(self,event_id) : 
		return Event.objects.get(id = event_id)

	def getAll(self):
		return Event.objects.all()

	def create(self, validated_data):
		EventAssembler().toPersistenObject(validated_data)
		instance = Event()
		instance.noun = validated_data.get('noun')

		instance.user_id = validated_data.get('user_id')
		instance.verb = validated_data.get('verb')
		instance.ts = validated_data.get('ts')
		instance.latlong = validated_data.get('latlong')
		instance.timespent = validated_data.get('timespent')
		instance.properties = validated_data.get('properties')
		instance.save()
		return instance

	def update(self, instance, validated_data):
		EventAssembler().toPersistenObject(validated_data)
		instance.noun = (validated_data.get('noun', instance.noun))
		instance.user_id = validated_data.get('user_id', instance.user_id)
		instance.ts = validated_data.get('ts', instance.ts)
		instance.latlong = validated_data.get('latlong', instance.latlong)
		instance.verb = validated_data.get('verb',instance.verb)
		instance.timespent = validated_data.get('timespent',instance.timespent)
		instance.properties = validated_data.get('properties',instance.properties)
		instance.save()
		return instance

