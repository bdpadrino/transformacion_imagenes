from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel

#class Post(models.Model):
#   title = models.CharField(max_length=4)
#   id = models.IntegerField(primary_key=True)
#   img = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)

class Post(TimeStampedModel, SoftDeletableModel):
	#title 				= models.CharField(max_length=50, null=False, blank=True)
	url_image			= models.URLField(null=False, blank=False)
	date_published 		= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated 		= models.DateTimeField(auto_now=True, verbose_name="date updated")
	def __str__(self):
		return self.title