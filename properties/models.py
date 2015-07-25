from ajaximage.fields import AjaxImageField
from django.db import models
from django.utils.text import slugify


class City(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(State, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class PinCode(models.Model):
    code = models.IntegerField(unique=True)

    def __unicode__(self):
        return unicode(self.code)


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
    connectivity = models.CharField(max_length=255, default=None, null=True)
    neighborhood_quality = models.CharField(max_length=255, default=None,
                                            null=True)
    comments = models.CharField(max_length=255, default=None, null=True)
    city = models.ForeignKey('City')
    state = models.ForeignKey('State', null=True, default=None)
    pin_code = models.ForeignKey('PinCode', null=True, default=None)
    developer = models.ForeignKey('Developer', null=True, default=None)
    owner = models.ForeignKey('Owner', null=True, default=None)
    created_by = models.ForeignKey('custom_user.User')

    project = models.ForeignKey('Project')

    def __unicode__(self):
        return self.property_type

    class Meta:
        verbose_name_plural = 'Properties'


class Developer(models.Model):
    name = models.CharField(max_length=255, null=False)
    number_of_projects = models.IntegerField(default=0)
    developer_report = models.CharField(max_length=255, null=True, default=None)

    def __unicode__(self):
        return self.name


class DeveloperProject(models.Model):
    project_name = models.CharField(max_length=255, null=False)
    launch_date = models.CharField(max_length=20, default=None, null=True)
    possession_date = models.CharField(max_length=20, default=None, null=True)
    location = models.CharField(max_length=255, default=None, null=True)
    other_status = models.CharField(max_length=255, default=None, null=True)
    status = models.CharField(max_length=255, default=None, null=True)
    address = models.TextField(default=None, null=True)
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
    status = models.CharField(max_length=255,null=True,
                                      default=None)
    permit_report = models.CharField(max_length=255, default=None,
                                     null=True)

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
    comment = models.TextField(default=None, null=True)

    def __unicode__(self):
        return self.project.name


class Owner(models.Model):
    name = models.CharField(max_length=255, null=False)
    occupation = models.CharField(max_length=255, default=None, null=True)
    pan_number = models.CharField(max_length=20, default=None, null=True)
    date_of_purchase = models.CharField(max_length=20, default=None, null=True)
    date_of_sale = models.CharField(max_length=20, default=None, null=True)
    # should be in property
    loan_status = models.BooleanField(default=False)
    loan_from = models.CharField(max_length=20, default=None, null=True)
    # should be in property
    main_cost_of_purchase = models.CharField(max_length=20, default=0)
    other_cost_1 = models.IntegerField(default=0)
    other_cost_2 = models.IntegerField(default=0)
    other_cost_3 = models.IntegerField(default=0)
    # should be in property?
    is_resale = models.BooleanField(default=False, choices=OWNER_CHOICES)
    name_of_seller = models.CharField(max_length=255, default=None, null=True)
    contact_number_seller = models.CharField(max_length=30, default=None,
                                             null=True)
    email_seller = models.EmailField(default=None, null=True)

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
