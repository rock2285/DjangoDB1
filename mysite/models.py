from django.db import models

class Item(models.Model):
  name = models.CharField(max_length=10)
  code = models.CharField(max_length=10)