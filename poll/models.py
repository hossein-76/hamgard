from django.contrib.postgres.fields import JSONField
from django.db import models


# Create your models here.

class PollChoice(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.pk


class PollQuestion(models.Model):
    text = models.CharField(max_length=200)
    choices = models.ManyToManyField(PollChoice, blank=True)

    def __str__(self):
        return self.pk


class PollCategory(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.pk


class GroupPoll(models.Model):
    group = models.ForeignKey('account.Group', on_delete=models.CASCADE)
    statistics = JSONField(blank=True, null=True)
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE)

    def __str__(self):
        return self.pk


class Poll(models.Model):
    questions = models.ManyToManyField(PollQuestion)
    category = models.ForeignKey(PollCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.pk
