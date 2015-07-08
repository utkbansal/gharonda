from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from models import Property, Developer, DeveloperProject, Owner, Bank, \
    Permissions, Project, Tower, ProjectPermission, State, City, PinCode

admin.site.register(Property)
admin.site.register(Developer)
admin.site.register(DeveloperProject)
admin.site.register(Owner)
# admin.site.register(Bank)
admin.site.register(Permissions)
# admin.site.register(Project)
admin.site.register(Tower)
# admin.site.register(ProjectPermission)
admin.site.register(State)
admin.site.register(City)
admin.site.register(PinCode)


class BankResource(resources.ModelResource):
    class Meta:
        model = Bank


class BankAdmin(ImportExportModelAdmin):
    resource_class = BankResource


admin.site.register(Bank, BankAdmin)


class ProjectPermissionResource(resources.ModelResource):
    class Meta:
        model = ProjectPermission
        fields = ('id', 'project__name', 'permission__name', 'value')


class ProjectPermissionAdmin(ImportExportModelAdmin):
    resource_class = ProjectPermissionResource


admin.site.register(ProjectPermission, ProjectPermissionAdmin)


class ProjectResource(resources.ModelResource):
    class Meta:
        model = Project
        fields = ('id', 'name', 'launch_date', 'possession_date', 'bank')


class ProjectAdmin(ImportExportModelAdmin):
    resource_class = ProjectResource


admin.site.register(Project, ProjectAdmin)
