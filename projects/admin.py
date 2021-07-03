from django.contrib import admin
from .models import Project,tags

# Register your models here.
admin.site.register(Project)
admin.site.register(tags)