

class Notification_Enable_Type(object):		
	Notification_Enable_Type_List = (
	    ('0', 'true'),
	    ('1', 'false'),
	    ('2', 'condtional'),
	)

	def getTypes(self):
		return self.Notification_Enable_Type_List