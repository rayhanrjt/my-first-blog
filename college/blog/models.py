from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
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

class Classs(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class student(models.Model):
    classs=models.ForeignKey(Classs,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    std_id = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    def __str__(self):              # __unicode__ on Python 2
        return self.classs

