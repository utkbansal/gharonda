from django.db import models

from django.contrib.auth.models import User


class BrokerProfile(models.Model):
    license_no = models.IntegerField(unique=True)
    user = models.OneToOneField(User)
    contact_no = models.IntegerField()
    company = models.ForeignKey('Company')

# More user info? UserProfile


class ContactNumber(models.Model):
    contact_no = models.IntegerField(unique=True)
    user = models.ForeignKey(User)


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()