from django.db import models
from django.contrib.postgres.fields import JSONField


# Create your models here.

class Travel(models.Model):
    group = models.ForeignKey('account.Group', on_delete=models.CASCADE)
    route = JSONField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=500)
    code = models.CharField(unique=True, max_length=40)
    used_events = JSONField(null=True, blank=True)

    def __str__(self):
        return self.pk


class Tour(models.Model):
    super_group = models.ForeignKey('account.SuperGroup', on_delete=models.CASCADE)
    route = JSONField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=500)
    code = models.CharField(unique=True, max_length=40)
    used_events = JSONField(null=True, blank=True)

    def __str__(self):
        return self.pk
