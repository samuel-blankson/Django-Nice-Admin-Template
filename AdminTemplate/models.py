from django.db import models

# Create your models here.


class Location(models.Model):
    Country = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    Gps = models.CharField(max_length=50)


class Todo(models.Model):
    subject = models.CharField(max_length=100)
    dateTime = models.DateTimeField(max_length=50)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE
    )
    todoType = models.CharField(max_length=50)
    description = models.TextField()
