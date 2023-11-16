from django.contrib import admin

from skills.models import SkillModel
# Register your models here.


class SkillAdmin(admin.ModelAdmin):
    pass


admin.site.register(SkillModel, SkillAdmin)
