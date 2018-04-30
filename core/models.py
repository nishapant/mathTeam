from django.db import models
# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
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


class Question(models.Model):
    grade = models.CharField(max_length=250)
    topic = models.CharField(max_length=250)
    description = models.TextField(default="", blank=True)
    answer = models.CharField(max_length=250, default="1")
    questionPicture = models.FileField()
    answerPicture = models.FileField()
    difficulty = models.CharField(max_length=250)
    year = models.CharField(max_length=250)
    created_date = models.DateTimeField(
            default=timezone.now)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.topic + " " + self.year
