from django.db import models
from Core.Noun.models import *
from Core.Verb.models import *
from Core.JSONField import JSONField
from FrameWork.Users_And_Groups.models import *
from datetime import datetime
# Create your models here.

class Event(models.Model):
	id = models.AutoField(primary_key=True)
	noun = models.ForeignKey(Noun,blank=True,null = True)
	user_id = models.ForeignKey(UserProfile)
	ts = models.CharField(max_length = 15)
	latlong = models.CharField(max_length = 15)
	verb = models.ForeignKey(Verb)
	timespent = models.IntegerField()
	properties = JSONField(blank=True, null=True)
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.noun.noun + self.verb.verb