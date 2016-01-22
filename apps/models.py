from django.db import models

# Create your models here.
class List(models.Model):
	pass


class Item(models.Model):
	text = models.CharField(default='', max_length=255, help_text="Tidak boleh melebihi 255 karakter.")
	list = models.ForeignKey(List, default=None, null=True)