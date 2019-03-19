from django.db import models


# Create your models here.

class TagCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name_fa = models.CharField(max_length=200, blank=True, null=True)
    name_en = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(TagCategory, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_fa
