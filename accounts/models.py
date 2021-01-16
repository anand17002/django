from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
	pass
	#phone = models.CharField(max_length=10, unique=True)
	#lname = models.CharField(max_length=200)
	#uname = models.CharField(max_length=200, unique=true)
	#email = models.CharField(max_lenth=200, unique=true)
	#updated = models.DateTimeField(auto_now= True)
	#created = models.DateTimeField(auto_now_add=True)
	date_of_birth = models.DateField(default=None)

	#REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
	def __str__(self):
		return self.username

