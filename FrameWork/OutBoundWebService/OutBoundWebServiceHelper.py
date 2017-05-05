from FrameWork.OutBoundWebService.OutBoundWebServiceSerializer import OutBoundWebServiceSerializer
from bankOnCube.logger import log
import urllib2,urllib

class OutBoundWebServiceHelper(object):
	

	def publish(self,data):
		config = OutBoundWebServiceSerializer().getValue('Notification.url', 'EndPointConfig')
		url = config.prop_value
		try:
			result = urllib2.urlopen(url, urllib.urlencode(data))
		except Exception,e:
			log.error(e)
