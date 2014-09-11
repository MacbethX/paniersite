from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title




class Meter(models.Model):
    mac = models.CharField('meter mac', max_length=100)
    transformer = models.CharField('meter transformer', max_length=100)
    longitute = models.DecimalField(max_digits=10, decimal_places=6, null=True,
            blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True,
            blank=True)


    def __unicode__(self):
        return self.mac

