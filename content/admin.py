from django.contrib import admin
from .models import Project, Skill

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'repository', 'live_link')
    fields = ('name', 'description', 'year', 'image', 'repository', 'live_link', 'skills')

admin.site.register(Skill)
