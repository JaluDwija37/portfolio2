from django.db import models

from programing_language.models import ProgLangModel


class SkillModel(models.Model):
    program = models.ForeignKey(ProgLangModel, on_delete=models.CASCADE)
    level = models.CharField(
        max_length=50,
        choices=[
            ('pemula', 'Pemula'),
            ('menengah', 'Menengah'),
            ('mahir', 'Mahir'),
            ('ahli', 'Ahli')
        ],
        default='pemula'
    )

    def __str__(self):
        return "{} - {}".format(self.program.name, self.level)
