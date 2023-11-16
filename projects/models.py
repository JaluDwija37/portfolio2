from django.db import models
from programing_language.models import ProgLangModel
# Create your models here.


class ProjectModel(models.Model):
    name = models.CharField(max_length=200)
    program = models.ManyToManyField(ProgLangModel)
    description = models.TextField()
    link_src = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True,
                              upload_to="image/projects/")

    def __str__(self):
        return "{} - {}".format(self.name, self.link_src)
