from django.db import models
class Item(models.Model):
    text=models.CharField(max_length=200)
    pub_date=models.DateTimeField()
# Create your models here.
