from django.db import models


# Create your models here.
class EventCategory(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.pk


class Event(models.Model):
    title_fa = models.CharField(max_length=500)
    title_en = models.CharField(max_length=500, blank=True, null=True)
    address = models.ForeignKey("place.Address", on_delete=models.CASCADE)
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    summary = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(default=0)
    discount = models.FloatField(null=True, blank=True)
    price = models.FloatField()
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.title_fa


class EventImage(models.Model):
    Event = models.ForeignKey(Event, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField()
    alt = models.CharField(max_length=100)

    def __str__(self):
        return self.pk

class EventVideo(models.Model):
    Event = models.OneToOneField(Event, related_name="video", on_delete=models.CASCADE)
    video = models.FileField()
    alt = models.CharField(max_length=100)

    def __str__(self):
        return self.pk
