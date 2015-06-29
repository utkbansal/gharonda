from django.contrib import admin

from models import Property, Developer, DeveloperProject, Owner, Bank, \
    Permissions, Project, Tower, ProjectPermission

admin.site.register(Property)
admin.site.register(Developer)
admin.site.register(DeveloperProject)
admin.site.register(Owner)
admin.site.register(Bank)
admin.site.register(Permissions)
admin.site.register(Project)
admin.site.register(Tower)
admin.site.register(ProjectPermission)