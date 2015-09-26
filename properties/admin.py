from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from models import Property, Developer, DeveloperProject, Owner, Bank, \
    Permissions, Project, Tower, ProjectPermission, State, City, PinCode


class BankResource(resources.ModelResource):
    class Meta:
        model = Bank


class BankAdmin(ImportExportModelAdmin):
    resource_class = BankResource
    ordering = ['name', ]


admin.site.register(Bank, BankAdmin)


class CityResource(resources.ModelResource):
    class Meta:
        model = City


class CityAdmin(ImportExportModelAdmin):
    resource_class = CityResource


admin.site.register(City, CityAdmin)


class DeveloperResource(resources.ModelResource):
    class Meta:
        model = Developer


class DeveloperAdmin(ImportExportModelAdmin):
    resource_class = DeveloperResource


admin.site.register(Developer, DeveloperAdmin)


class PinCodeResource(resources.ModelResource):
    class Meta:
        model = PinCode


class PinCodeAdmin(ImportExportModelAdmin):
    resource_class = PinCodeResource


admin.site.register(PinCode, PinCodeAdmin)


class StateResource(resources.ModelResource):
    class Meta:
        model = State


class StateAdmin(ImportExportModelAdmin):
    resource_class = StateResource


admin.site.register(State, StateAdmin)


class TowerResource(resources.ModelResource):
    class Meta:
        model = Tower


class TowerAdmin(ImportExportModelAdmin):
    resource_class = TowerResource


admin.site.register(Tower, TowerAdmin)


class PermissionsResource(resources.ModelResource):
    class Meta:
        model = Permissions


class PermissionAdmin(ImportExportModelAdmin):
    resource_class = PermissionsResource


admin.site.register(Permissions, PermissionAdmin)


class OwnerResource(resources.ModelResource):
    class Meta:
        model = Owner


class OwnerAdmin(ImportExportModelAdmin):
    resource_class = OwnerResource


admin.site.register(Owner, OwnerAdmin)


class DeveloperProjectResource(resources.ModelResource):
    class Meta:
        model = DeveloperProject


class DeveloperProjectAdmin(ImportExportModelAdmin):
    resource_class = DeveloperProjectResource


admin.site.register(DeveloperProject, DeveloperProjectAdmin)


class PropertyResource(resources.ModelResource):
    class Meta:
        model = Property


class PropertyAdmin(ImportExportModelAdmin):
    resource_class = PropertyResource


admin.site.register(Property, PropertyAdmin)


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
