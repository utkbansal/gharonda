import binascii
import os

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email or not password:
            raise ValueError('User must have a username and password')

        user = self.model(
            email=CustomUserManager.normalize_email(email),
            **kwargs
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)

        user.is_admin = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False, unique=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff

    class Meta:
        ordering = ('created_on',)
        db_table = 'users'

    def __unicode__(self):
        return self.get_full_name()


class AccessToken(models.Model):
    access_token = models.CharField(max_length=50, primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    device_id = models.CharField(max_length=255, default=None)
    device_type = models.CharField(max_length=10, default=None)
    push_id = models.CharField(max_length=255, default=None)
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.access_token:
            self.access_token = self.generate_token()
            return super(AccessToken, self).save(*args, **kwargs)

    def generate_token(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.access_token


class BrokerProfile(models.Model):
    license_no = models.CharField(max_length=255)
    user = models.OneToOneField(User)
    company = models.ForeignKey('Company')

    def __unicode__(self):
        return self.user.get_full_name()


class ContactNumber(models.Model):
    contact_no = models.CharField(max_length=255)
    contact_type = models.CharField(max_length=255, default='Mobile')
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.contact_no


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __unicode__(self):
        return self.name