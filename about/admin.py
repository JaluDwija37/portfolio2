from django.contrib import admin

# Register your models here.

from about.models import AboutModel


class AboutModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(AboutModel, AboutModelAdmin)
