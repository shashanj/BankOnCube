from django.db import models
from django.contrib.auth.models import User
from FrameWork.Users_And_Groups.models import *
from Core.Noun.models import *
# Create your models here.

class Roles(models.Model):
	roleCode = models.CharField(max_length=100, blank=False,null=False)
	title = models.CharField(max_length=100, blank=True, default='')
	description = models.CharField(max_length=100, blank=True, default='')
	isActive = models.BooleanField(default=True)
	allowedNoun = models.ManyToManyField(Noun)
	
	class Meta:
		ordering = ('title',)

	def __str__(self):
		return self.title


class UserRoles(models.Model):
 	usersRole = models.OneToOneField(UserProfile)
 	intendedRoles = models.ManyToManyField(Roles)
 	
 	def __str__(self):
		return self.usersRole.usr.first_name
 		