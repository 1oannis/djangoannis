"""Polls models"""

import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """Question model"""

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        """String representation of Question"""
        return self.question_text

    def was_published_recently(self):
        """Returns True if this question has been published recently, else False"""
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    """Choice model"""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """String representation of Choice"""
        return self.choice_text
