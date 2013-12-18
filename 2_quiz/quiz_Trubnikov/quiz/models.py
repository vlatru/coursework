# Create your models here.
from datetime import datetime
from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True, db_index=True, default=datetime.now())
    updated = models.DateTimeField(
        auto_now=True, db_index=True, default=datetime.now())

    class Meta:
        abstract = True


class Question(TimeStampedModel):
    que_text = models.TextField('Question')

    def get_absolute_url(self):
        return "/quiz/%s/" % self.id

    def __unicode__(self):
        return self.que_text


class Answer(models.Model):
    que_id = models.ForeignKey(Question)
    ans_text = models.TextField()
    freq = models.IntegerField(default=0)

    def __unicode__(self):
        return self.ans_text
