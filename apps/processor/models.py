from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=200)
	lastedit_date = models.DateTimeField()

	def get_absolute_url(self):
		return "/p/%i/" % self.id

# Create your models here.
