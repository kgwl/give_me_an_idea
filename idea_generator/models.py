from django.db import models


class Category(models.Model):
    """
    Stores a categories for Idea model.
    """
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category

class Difficulties(models.Model):
    """
    Stores difficulty levels for Idea model.
    """
    id = models.AutoField(primary_key=True)
    difficulty = models.CharField(max_length=100)

    def __str__(self):
        return self.difficulty

class Idea(models.Model):
    """
    Stores programming project ideas.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    difficulty = models.ForeignKey(Difficulties,on_delete=models.PROTECT)
    description = models.TextField(max_length=200)
