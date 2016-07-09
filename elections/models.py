from django.db import models

# Create your models here.

class Candidate(models.Model):
    name = models.CharField(max_length = 10)
    introduction = models.TextField()
    category = models.CharField(max_length = 15)
    number = models.IntegerField(default = 0)

    def __str__(self):
        return self.name


class Poll(models.Model):
    name = models.CharField(max_length = 10)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    candidate = models.ForeignKey(Candidate)
    votes = models.IntegerField(default = 0)
