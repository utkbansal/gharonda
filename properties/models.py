from django.db import models


class Property(models.Model):
    property_type = models.CharField(max_length=255, default='Apartment')
    specifications = models.CharField(max_length=255, default='Basic')
    built_up_area = models.FloatField(max_length=6, null=False)
    total_area = models.FloatField(null=False)
    number_of_bedrooms = models.CharField(max_length=3, default=1)
    number_of_bathrooms = models.CharField(max_length=3, default=1)
    number_of_parking_spaces = models.CharField(max_length=2, default=0)
    address_line_one = models.CharField(max_length=255, null=False)
    address_line_two = models.CharField(max_length=255, default=None)
    city = models.CharField(max_length=255, null=False)
    state = models.CharField(max_length=255, null=False)
    pin_code = models.CharField(max_length=20, null=False)
    developer = models.ForeignKey('Developer')

    connectivity = models.CharField(max_length=255, default=None, null=True)
    neighborhood_quality = models.CharField(max_length=255, default=None, null=True)
    comments = models.CharField(max_length=255, default=None, null=True)

    def __unicode__(self):
        return self.property_type


class Developer(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __unicode__(self):
        return self.name


class DeveloperProjects(models.Model):
    project_name = models.CharField(max_length=255, null=False)
    launch_date_month = models.CharField(max_length=20, default='')
    launch_date_year = models.CharField(max_length=4, default='')
    possession_date_month = models.CharField(max_length=20, default='')
    possession_date_year = models.CharField(max_length=4, default='')
    location = models.CharField(max_length=255, default='')
    other_status = models.CharField(max_length=255, default='')

    def __unicode__(self):
        return self.project_name


class Project(models.Model):
    name = models.CharField(max_length=255, null=False)
    launch_date = models.CharField(max_length=20, null=False)
    possession_date = models.CharField(max_length=20, null=False)
    # Permit
    # Contractors
    # Loans Available

    def __unicode__(self):
        return self.name


class Owner(models.Model):
    name = models.CharField(max_length=255, null=False)
    occupation = models.CharField(max_length=255, null=False)
    pan_number = models.CharField(max_length=20, default=None)
    date_of_purchase = models.CharField(max_length=20, default=None)
    loan_from = models.CharField(max_length=20, default=None)
    cost_of_purchase = models.CharField(max_length=20, default=0)
    is_resale = models.BooleanField(default=False)
    name_of_seller = models.CharField(max_length=255, default=None)
    contact_number_seller = models.CharField(max_length=30, default=None)
    email_seller = models.CharField(max_length=255, default=None)

    def __unicode__(self):
        return self.name