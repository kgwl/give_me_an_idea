from django.db import models

class Idea(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200,default='default')
    difficulty = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    language_category = models.IntegerField()
