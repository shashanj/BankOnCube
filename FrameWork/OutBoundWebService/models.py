from django.db import models

# Create your models here.
class BC_FW_CONFIG_VAR_B(models.Model):

	prop_id = models.CharField(max_length = 40, primary_key = True)
	prop_value = models.CharField(max_length = 100)
	category = models.CharField(max_length = 100)
	desc = models.TextField()


	def __str__(self):
		return self.prop_id