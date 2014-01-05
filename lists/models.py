from django.db import models

# Create your models here.
class List(models.Model):
    pass

class Item(models.Model):
	text = models.TextField()
	list = models.ForeignKey(List)
