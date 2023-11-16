from django.contrib import admin

# Register your models here.

from certificates.models import CertificateModel


class CertificateModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(CertificateModel, CertificateModelAdmin)
