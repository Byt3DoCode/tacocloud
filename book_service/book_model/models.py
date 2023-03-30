from django.db import models

# Create your models here.


class books(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    availability = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.id, self.name, self.author, self.availability, self.description, self.price)
