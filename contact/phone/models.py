from django.db import models

# Create your models here.
class Contacts(models.Model):
    Name=models.CharField(max_length=50)
    Number=models.IntegerField(max_length=15)
    


    def __str__(self):
        return self.Name
