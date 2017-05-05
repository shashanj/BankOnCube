from django.db import models
from Core.Verb.models import *
from Core.Noun.NotificationEnableType import *
# Create your models here.

class Noun(models.Model):
	noun_code = models.CharField(primary_key=True,max_length=10, blank=False,null=False)
	noun =  models.CharField(max_length=30, blank=False,null=False)
	desc = models.CharField(max_length=100)
	allowedVerb = models.ManyToManyField(Verb)

	def __str__(self):
		return self.noun


# class Notification_Config(models.Model):
# 	noun = models.ForeignKey(Noun)
# 	verb = models.ForeignKey(Verb)
# 	notification_enable = models.CharField(max_length=3,choices = Notification_Enable_Type().getTypes())
# 	condition = models.TextField(null= True)
# 	expected_output_type  = models.CharField(max_length=100)
# 	expected_output = models.CharField(max_length=100)

# 	def __str__(self):
# 		return self.noun.noun + self.verb.verb