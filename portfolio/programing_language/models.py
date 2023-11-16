from django.db import models

# Create your models here.


class ProgLangModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True,
                              upload_to="image/prog_language/")

    def __str__(self):
        return "{}".format(self.name)
