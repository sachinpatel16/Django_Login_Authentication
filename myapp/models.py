from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    # mobileNumber = models.IntegerField(max_length=10, unique=True)
    password = models.CharField(max_length = 225)
    # confirmPassword =