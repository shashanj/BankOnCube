from Config.NotificationConstants import NotificationConstants
import logging

from bankOnCube.logger import log

class NotificationMocked(object):

	def post(self,request):
		recepint = request.get(NotificationConstants.RECEIPIENT)
		group = request.get(NotificationConstants.ISGROUP)
		message = request.get(NotificationConstants.MESSAGE)

		log.warning(request)