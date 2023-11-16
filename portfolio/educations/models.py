from django.db import models

# Create your models here.


class EducationModel(models.Model):
    name = models.CharField(max_length=200, default=None)
    major = models.CharField(max_length=200, default=None)
    grade = models.CharField(max_length=10, default=None)
    year_start = models.DateField(null=False, default=None)
    year_end = models.DateField(null=False, default=None)

    def __str__(self):
        return "{} - {}".format(self.name, self.major)
