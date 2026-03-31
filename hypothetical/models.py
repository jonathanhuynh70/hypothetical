from django.db import models
from django.utils import timezone
import datetime

class User(models.Model):
    partner = models.ForeignKey("self", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    edittable = models.BooleanField()

    def was_published_recently(self):
        return timezone.now() > self.pub_date > datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comments(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)

class Votes(models.Model):
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)


