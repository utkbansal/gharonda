from ajaximage.fields import AjaxImageField
from django.db import models


class Property(models.Model):
    property_type = models.CharField(max_length=255, default='Apartment')
    specifications = models.CharField(max_length=255, default='Basic')
    built_up_area = models.FloatField(max_length=6, null=False, default=0)
    total_area = models.FloatField(null=False, default=0)
    number_of_bedrooms = models.CharField(max_length=3, default=1)
    number_of_bathrooms = models.CharField(max_length=3, default=1)
    number_of_parking_spaces = models.CharField(max_length=2, default=0)
    address_line_one = models.CharField(max_length=255, null=False)
    address_line_two = models.CharField(max_length=255, null=True, default=None)
    city = models.CharField(max_length=255, null=False)
    state = models.CharField(max_length=255, null=False)
    pin_code = models.CharField(max_length=20, null=False)
    developer = models.ForeignKey('Developer', null=True, default=None)
    owner = models.ForeignKey('Owner', null=True, default=None)

    connectivity = models.CharField(max_length=255, default=None, null=True)
    neighborhood_quality = models.CharField(max_length=255, default=None,
                                            null=True)
    comments = models.CharField(max_length=255, default=None, null=True)
    created_by = models.ForeignKey('custom_user.User')

    project = models.ForeignKey('Project')

    def __unicode__(self):
        return self.property_type

    class Meta:
        verbose_name_plural = 'Properties'


class Developer(models.Model):
    name = models.CharField(max_length=255, null=False)
    number_of_projects = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class DeveloperProject(models.Model):
    project_name = models.CharField(max_length=255, null=False)
    launch_date = models.CharField(max_length=20, default=None, null=True)
    possession_date = models.CharField(max_length=20, default=None, null=True)
    location = models.CharField(max_length=255, default=None, null=True)
    other_status = models.CharField(max_length=255, default=None, null=True)
    developer = models.ForeignKey('Developer')

    def __unicode__(self):
        return self.project_name


class Bank(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255, null=False)
    launch_date = models.CharField(max_length=20, null=False)
    possession_date = models.CharField(max_length=20, null=False)
    contractor_name_1 = models.CharField(max_length=255, null=True,
                                         default=None)
    contractor_name_2 = models.CharField(max_length=255, null=True,
                                         default=None)
    contractor_name_3 = models.CharField(max_length=255, null=True,
                                         default=None)
    bank = models.ManyToManyField('Bank')

    def __unicode__(self):
        return self.name


OWNER_CHOICES = ((True, 'Re-Sale'), (False, 'Direct Builder'))


class Permissions(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class ProjectPermission(models.Model):
    project = models.ForeignKey('Project')
    permission = models.ForeignKey('Permissions')
    value = models.CharField(max_length=255)

    def __unicode__(self):
        return self.project.name


class Owner(models.Model):
    name = models.CharField(max_length=255, null=False)
    occupation = models.CharField(max_length=255, default=None, null=True)
    pan_number = models.CharField(max_length=20, default=None, null=True)
    date_of_purchase = models.CharField(max_length=20, default=None, null=True)
    # should be in property
    loan_from = models.CharField(max_length=20, default=None, null=True)
    # should be in property
    main_cost_of_purchase = models.CharField(max_length=20, default=0)
    other_cost_1 = models.IntegerField(default=0)
    other_cost_2 = models.IntegerField(default=0)
    # should be in property?
    is_resale = models.BooleanField(default=False, choices=OWNER_CHOICES)
    name_of_seller = models.CharField(max_length=255, default=None, null=True)
    contact_number_seller = models.CharField(max_length=30, default=None,
                                             null=True)
    email_seller = models.CharField(max_length=255, default=None, null=True)

    co_owner = models.ForeignKey('Owner', null=True, default=None)

    def __unicode__(self):
        return self.name


class Tower(models.Model):
    name = models.CharField(max_length=255)
    floors_completed = models.IntegerField(default=0)
    finishing_status = models.CharField(max_length=255, default=None, null=True)
    other_status = models.CharField(max_length=255, default=None, null=True)
    image = AjaxImageField(upload_to='pics', default=None, null=True)
    project = models.ForeignKey('Project')

    def __unicode__(self):
        return self.name
