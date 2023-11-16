from django.contrib import admin

# Register your models here.
from educations.models import EducationModel


class EducationModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(EducationModel, EducationModelAdmin)
