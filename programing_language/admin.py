from django.contrib import admin

# Register your models here.
from programing_language.models import ProgLangModel


class ProgLangAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProgLangModel, ProgLangAdmin)
