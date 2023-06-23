from django.db import models
from django.forms.widgets import DateInput

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='images')
    desc = models.TextField()

    def __str__(self):
        return self.name

