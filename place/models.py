from django.db import models


# Create your models here.


class Province(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class City(models.Model):
    province = models.ForeignKey(Province, related_name="cities", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True, default=None)
    lng = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name


class Address(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    address_text = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.pk


class PlaceCategory(models.Model):
    name_fa = models.CharField(max_length=500)
    name_en = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name_fa


class Place(models.Model):
    name_fa = models.CharField(max_length=500)
    name_en = models.CharField(max_length=500, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    tags = models.ManyToManyField('tag.Tag', blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    category = models.ForeignKey(PlaceCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_fa
