from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from Modules.Events.views import *
from Modules.Events.models import *
from Modules.Events.EventsSerializer import EventsSerializer
from Modules.Events.ValidateEvent import ValidateEvent
from django.db import connection
from FrameWork.QueryHelper import QueryHelper
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from Config.QueryConstants import QueryConstants
from Config.NotificationConstants import NotificationConstants
from Modules.Events.EventBusinessHelper import EventBusinessHelper
import urllib2,urllib

class EventList(APIView):

	def get(self, request):
		event = EventsSerializer().getAll()
		serializer = EventsSerializer(event, many = True)
		return Response(serializer.data)

	def post(self, request):
		validat = ValidateEvent()
		validat.validateInput(request)
		if(validat.isvalid()):
			event = EventsSerializer().create(request.data.copy())
			serializer = EventsSerializer(event)

			###### post hook extentions #################
			EventBusinessHelper().help(request)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			try:
				error = {"error" : validat.getError() , "status" : status.HTTP_400_BAD_REQUEST}
				return Response(error, status=status.HTTP_400_BAD_REQUEST)
			except :
				error = {"error" : validat.getError()[0] , "status" : status.HTTP_401_BAD_REQUEST}
				return Response(error, status=status.HTTP_400_BAD_REQUEST)


class EventDetails(APIView):

	def get(self, request, pk):
		event = EventsSerializer().get(pk)
		serializer = EventsSerializer(event, many = False)
		return Response(serializer.data)

		
			


			
		

