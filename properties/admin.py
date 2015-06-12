from django.contrib import admin

from models import Property, Developer, DeveloperProjects, Owner

admin.site.register(Property)
admin.site.register(Developer)
admin.site.register(DeveloperProjects)
admin.site.register(Owner)
