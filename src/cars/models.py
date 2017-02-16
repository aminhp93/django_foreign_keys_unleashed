from django.conf import settings
from django.db import models

# Create your models here.
User = settings.AUTH_USER_MODEL

class Car(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=120)

	def __str__(self):
		return self.name