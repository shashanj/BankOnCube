from FrameWork.QueryHelper import QueryHelper
from Config.QueryConstants import QueryConstants
from Config.NotificationConstants import NotificationConstants
from FrameWork.OutBoundWebService.OutBoundWebServiceHelper import OutBoundWebServiceHelper
import ast,json,time,threading


class EventBusinessHelper(object):


	def help(self,request):
		self.publishFirstBillPay(request)
		self.alertForBillPay(request)
		self.alertNoFeedback(request)


	def publishFirstBillPay(self,request):
		clazz =  QueryHelper.execute(QueryConstants.EVENT, request.data)
		if(len(clazz) == 1):
			post_data= {}
			post_data[NotificationConstants.RECEIPIENT] = request.data.get('user_id')
			post_data[NotificationConstants.ISGROUP] = False
			post_data[NotificationConstants.MESSAGE] = "First Bill Pay Succesfull"
			OutBoundWebServiceHelper().publish(post_data)

	def alertForBillPay(self,request):
		clazz =  QueryHelper.execute(QueryConstants.EVENT, request.data).order_by('-created_on',)
		count = 0
		finalevent  = []
		for clss in  clazz :
			print clss.created_on
			dictt = ast.literal_eval(clss.properties)
			if(int(dictt['value']) >= 20000):
				count = count + 1
				if(count == 5):
					finalevent.append(clss)
					break
		try :
			recenttime = finalevent[0].created_on
			finaltime = clazz[0].created_on			
			delta =  (finaltime - recenttime).total_seconds()
			if(delta < 1200) : 
				post_data= {}
				post_data[NotificationConstants.RECEIPIENT] = request.data.get('user_id')
				post_data[NotificationConstants.ISGROUP] = False
				post_data[NotificationConstants.MESSAGE] = "Check Ckeck!!!!!!!!!!!!!!!!!!!!!!!!"
				OutBoundWebServiceHelper().publish(post_data)
		except Exception,e:
			pass

	def alertNoFeedback(self,request):
		if(request.data.get('noun') == 'bill' and request.data.get('verb')=='pay'):
			threadd = threading.Thread(target=self.waitForFeedBack, args=(request,), kwargs={})
			threadd.setDaemon(True)
			threadd.start()

	def waitForFeedBack(self,request):
		time.sleep(20)
		data = {}
		data['user_id'] = request.data.get('user_id') 
		data['noun'] = 'fdbk'
		data['verb'] = 'post'
		clazz =  QueryHelper.execute(QueryConstants.EVENT, request.data).order_by('-created_on',)
		feedback =  QueryHelper.execute(QueryConstants.EVENT, data).order_by('-created_on',)

		if(len(clazz) != len(feedback)):
			post_data= {}
			post_data[NotificationConstants.RECEIPIENT] = request.data.get('user_id')
			post_data[NotificationConstants.ISGROUP] = False
			post_data[NotificationConstants.MESSAGE] = "FeedBack Not Provided By User : " + request.data.get('user_id')
			OutBoundWebServiceHelper().publish(post_data)

