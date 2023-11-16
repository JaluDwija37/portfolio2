from django.contrib import admin

# Register your models here.
from projects.models import ProjectModel
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProjectModel, ProjectAdmin)
