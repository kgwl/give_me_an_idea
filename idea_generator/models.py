from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=200)

class Difficulties(models.Model):
    id = models.AutoField(primary_key=True)
    difficulty = models.CharField(max_length=100)

class Idea(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    difficulty = models.ForeignKey(Difficulties,on_delete=models.PROTECT)
    description = models.TextField(max_length=500)
