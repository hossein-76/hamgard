from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Vendor(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    national_number = models.CharField(max_length=500, blank=True, null=True, default=None)
    business_license = models.CharField(max_length=500, blank=True, null=True, default=None)
    name = models.CharField(max_length=500, blank=True, null=True, default=None)
    approval_status = models.CharField(default="pending", max_length=10, choices=(("pending", "pending"),
                                                                                  ("approved", "approved"),
                                                                                  ("rejected", "rejected")))
    reason = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.pk


class User(AbstractUser):
    mobile_number = models.CharField(max_length=500, blank=True, null=True, default=None)
    email_is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=40, null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    remember_me = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Group(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, related_name="user_groups", on_delete=models.CASCADE)
    members = models.ManyToManyField(User, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(null=True, blank=True, max_length=200)


class SuperGroup(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, blank=True, related_name='super_members')

    def __str__(self):
        return self.pk
