from django.db import models

# Create your models here.

class Verb(models.Model):
	verb_code = models.CharField(primary_key=True,max_length=10, blank=False,null=False)
	verb =  models.CharField(max_length=30, blank=False,null=False)
	desc = models.CharField(max_length=100)

	def __str__(self):
		return self.verb