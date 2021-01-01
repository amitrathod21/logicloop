from django.db import models

# Create your models here.


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    title= models.CharField(max_length=25)
    description = models.TextField(max_length=100)
    done = models.BooleanField()

    def __str__(self):
        return self.title