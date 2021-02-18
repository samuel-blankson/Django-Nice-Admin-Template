from django.db import models

# Create your models here.


class Todo:
    id: int
    subject: str
    date: str
    location: str
    todoType: str
    description: str
