from django.db import models
from django.shortcuts import resolve_url

# Create your models here.
class List(models.Model):
    def get_absolute_url(self):
        return resolve_url('view_list', self.id)

class Item(models.Model):
	text = models.TextField()
	list = models.ForeignKey(List)

	def save(self,*args,**kwargs):
		self.full_clean()
		super(Item,self).save(*args,**kwargs)
