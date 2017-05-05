from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
	user_id = models.CharField(primary_key=True,max_length=20, blank=False,null=False)
	usr =  models.OneToOneField(User)
	readOnly = models.BooleanField(default=False)


	############## Future Scope ############
	# link Contact And Address And other info of user_id
	########################################
	class Meta:
		ordering = ('user_id',)

	def __str__(self):
		return self.usr.first_name