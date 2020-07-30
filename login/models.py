from django.db import models
# Create your models here.
class User(models.Model):
    login=models.CharField(max_length=10)
    password=models.CharField(max_length=10)

    def __str__(self):
        return self.login



class Item(models.Model):
    user=models.ForeignKey("User",on_delete=models.CASCADE, default=0)
    text=models.CharField(max_length=200)
    pub_date=models.DateTimeField()
