from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from Config.NotificationConstants import NotificationConstants
from Modules.Notification.NotifyMocked import NotificationMocked

class Notification(APIView):

	def post(self,request):
		NotificationMocked().post(request.data)

		return Response({'success' : 'success'}, status=status.HTTP_200_OK)