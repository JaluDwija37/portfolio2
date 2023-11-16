from django.db import models

# Create your models here.


class CertificateModel(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    intitution = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True,
                              upload_to="image/cerificates/")

    def __str__(self):
        return "{}".format(self.name)
