from django.db import models

# Create your models here.


class AboutModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_description = models.TextField()
    long_description = models.TextField()

    def __str__(self):
        return "{}".format(self.name)
