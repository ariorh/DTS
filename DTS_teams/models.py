from django.db import models

# Create your models here.


class Teams(models.Model):

    title = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    description = models.TextField()
    pos1 = models.CharField(max_length=40)
    pos2 = models.CharField(max_length=40)
    pos3 = models.CharField(max_length=40)
    pos4 = models.CharField(max_length=40)
    pos5 = models.CharField(max_length=40)
    coach = models.CharField(max_length=40)
    achievements1 = models.TextField(default = "")
    achievements2 = models.TextField(default = "")
    achievements3 = models.TextField(default = "")
    achievements4 = models.TextField(default = "")
    upcoming_events = models.TextField(default = "")
    previous_members = models.TextField(default = "")
    logo = models.TextField(default = "")



    def __str__(self):
        return self.title
