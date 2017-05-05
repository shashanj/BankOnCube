from django.db import models

# Create your models here.

class Query(models.Model):
	id = models.CharField(max_length = 30, primary_key = True)
	modelName = models.CharField(max_length = 100)
	filters = models.TextField()
	args = models.TextField()
	desc = models.TextField()

	def __str__(self):
		return self.id
	