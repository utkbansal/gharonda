from crispy_forms.bootstrap import AppendedText, InlineRadios
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Field, Div
from django.forms import ModelForm
from django import forms

from models import (Property,
                    Owner,
                    Developer,
                    DeveloperProjects,
                    Project, ProjectPermission,
                    Bank,
                    Permissions)


class PermissionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PermissionForm, self).__init__(*args, **kwargs)

        permissions = Permissions.objects.all()
        for permission in permissions:
            self.fields[permission.name] = forms.CharField(
                widget=forms.Select(choices=(
                    ('Approved', 'Approved'),
                    ('In Process', 'In Process'),
                    ('Not Applied', 'Not Applied'),
                    ('Denied', 'Denied'),
                )))

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_id = 'permission-form'
        self.helper.add_input(
            Submit('project-details', 'submit', css_class='btn-block',
                   css_id='submit-project-details')
        )

    def save(self, *args, **kwargs):
        project = kwargs.pop('project')
        for field in self.fields:
            permission = Permissions.objects.filter(name=field).first()
            p = ProjectPermission(
                project=project,
                permission=permission,
                value=self.cleaned_data[field]
            )
            p.save()
        return project


class ProjectForm(ModelForm):
    add_bank = forms.BooleanField(required=False, label='Add a bank')
    new_bank = forms.CharField(required=False, label='Bank Name')

    class Meta:
        model = Project
        fields = [
            'name',
            'launch_date',
            'possession_date',
            'bank',
            'add_bank',
            'new_bank',
            'contractor_name_1',
            'contractor_name_2',
            'contractor_name_3',
        ]

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_id = 'project-form'
        self.fields['bank'].required = False
        self.fields['contractor_name_1'].required = False
        self.fields['contractor_name_2'].required = False
        self.fields['contractor_name_3'].required = False
        self.helper.layout = Layout(
            'name',
            Div(
                Field('launch_date', css_class='date-field'),
                css_class='col-md-6',
                style='padding-left:0px'
            ),
            Div(
                Field('possession_date',
                      css_class='date-field',
                      ),
                css_class='col-md-6',

                style='padding-right:0px'),
            'bank',
            'add_bank',
            'new_bank',
            'contractor_name_1',
            'contractor_name_2',
            'contractor_name_3',
        )

    def save(self, commit=True):
        if 'add_bank' in self.cleaned_data.keys():
            if self.cleaned_data['add_bank'] is True:
                bank = Bank(name=self.cleaned_data['new_bank'])

                project = super(ProjectForm, self).save()
                bank.save()
                project.bank.add(bank)
                return project
        return super(ProjectForm, self).save()


class PropertyBasicDetailsForm(ModelForm):
    developer_name = forms.CharField()
    project_name = forms.CharField()
    owner_name = forms.CharField()

    class Meta:
        model = Property
        fields = [
            'address_line_one',
            'address_line_two',
            'city',
            'state',
            'pin_code']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(PropertyBasicDetailsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_tag =False
        self.helper.form_id = 'project-basic-details-form'
        self.fields['address_line_two'].required = False
        self.helper.layout = Layout(
            # 'name',
            'owner_name',
            'project_name',
            'developer_name',
            'address_line_one',
            'address_line_two',
            'city',
            'state',
            'pin_code',
            ButtonHolder(
                Submit('Submit', 'submit', css_class='btn-block')
            )
        )

    def save(self, commit=True):
        developer_name = self.cleaned_data['developer_name']
        dev, created = Developer.objects.get_or_create(name=developer_name)
        self.instance.developer = dev

        self.instance.created_by = self.request.user
        return super(PropertyBasicDetailsForm, self).save()


MONTHS = (
    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'),
    ('April', 'April'),
    ('May', 'May'),
    ('June', 'June'),
    ('July', 'July'),
    ('August', 'August'),
    ('September', 'September'),
    ('October', 'October'),
    ('November', 'November'),
    ('December', 'December')
)


class DeveloperProjectForm(ModelForm):
    developer = forms.CharField()

    class Meta:
        model = DeveloperProjects
        fields = [
            'project_name',
            'launch_date',
            'possession_date',
            'number_of_projects',
        ]

    def __init__(self, *args, **kwargs):
        super(DeveloperProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'builder-details'
        self.helper.layout = Layout(
            'project_name',
            Div(
                Field('launch_date', css_class='month-year'),
                css_class='col-md-6',
                style='padding-left:0px'
            ),
            Div(
                Field('possession_date', css_class='month-year'),
                css_class='col-md-6',
                style='padding-right:0px'
            ),
            'developer',
            'number_of_projects',

            ButtonHolder(
                Submit('builder-details', 'submit', css_class='btn-block',
                       css_id='submit-builder-details')
            )
        )

    def save(self, commit=True):
        developer = self.cleaned_data['developer']
        developer, created = Developer.objects.get_or_create(name=developer)
        self.instance.developer = developer

        return super(DeveloperProjectForm, self).save()


OWNER_CHOICES = ((True, 'Re-Sale'), (False, 'Direct Builder'))


class OwnerForm(ModelForm):
    co_owner_name = forms.CharField()
    co_owner_occupation = forms.CharField()

    class Meta:
        model = Owner
        fields = [
            'name',
            'occupation',
            'pan_number',
            'date_of_purchase',
            'loan_from',
            'cost_of_purchase',
            'is_resale',
            'name_of_seller',
            'contact_number_seller',
            'email_seller',
        ]

        widgets = {
            'is_resale': forms.RadioSelect,
        }

    def __init__(self, *args, **kwargs):
        super(OwnerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_id = 'owner-form'
        self.fields['name_of_seller'].required = False
        self.fields['contact_number_seller'].required = False
        self.fields['email_seller'].required = False
        self.helper.layout = Layout(
            Div(
                Div('name',
                    'occupation',
                    'loan_from',
                    'pan_number',
                    css_class='col-md-6',
                    style='padding-left:0px'),

                Div('co_owner_name',
                    'co_owner_occupation',
                    'cost_of_purchase',

                    Field('date_of_purchase', css_class='date-field'),
                    css_class='col-md-6',
                    style='padding-right:0px'),
                InlineRadios('is_resale'),
                Div(
                    'name_of_seller',
                    css_class='col-md-6',
                    style='padding-left:0px'
                ),
                Div(
                    'contact_number_seller',
                    css_class='col-md-6',
                    style='padding-right:0px'
                ),

                'email_seller',
                ButtonHolder(
                    Submit('owner-details', 'submit', css_class='btn-block',
                           css_id='submit-owner-details')

                )
            )
        )

    def save(self, commit=True):
        co_owner_name = self.cleaned_data['co_owner_name']
        co_owner_occupation = self.cleaned_data['co_owner_occupation']

        co_owner, created = Owner.objects.get_or_create(
            name=co_owner_name,
            occupation=co_owner_occupation
        )

        self.instance.co_owner = co_owner

        return super(OwnerForm, self).save()


BEDROOM_CHOICE = []
for i in range(1, 11):
    BEDROOM_CHOICE.append(tuple((i, i)))

BEDROOM_CHOICE = tuple(BEDROOM_CHOICE)
BATHROOM_CHOICE = BEDROOM_CHOICE

PROPERTY_TYPE_CHOICE = (
    ('Apartment', 'Apartment'),
    ('Town Home', 'Town Home'),
    ('Single Family House', 'Single Family House'),
    ('Land', 'Land'),
)

SPECIFICATION_CHOICE = (
    ('Basic', 'Basic'),
    ('Premium', 'Premium'),
    ('Luxury', 'Luxury'),
)


class PropertyForm(ModelForm):
    developer = forms.CharField(label='Builder Name')

    class Meta:
        model = Property
        fields = [
            'property_type',
            'specifications',
            'built_up_area',
            'total_area',
            'number_of_bedrooms',
            'number_of_bathrooms',
            'number_of_parking_spaces',
            'address_line_one',
            'address_line_two',
            'city',
            'state',
            'pin_code',
        ]
        widgets = {
            'number_of_bedrooms': forms.Select(
                choices=BEDROOM_CHOICE, ),
            'number_of_bathrooms': forms.Select(
                choices=BATHROOM_CHOICE),
            'number_of_parking_spaces': forms.Select(
                choices=((1, 1,), (2, 2), ('3+', '3+')), ),
            'developer': forms.TextInput(),
            'property_type': forms.Select(choices=PROPERTY_TYPE_CHOICE),
            'specifications': forms.Select(choices=SPECIFICATION_CHOICE)
        }

    def __init__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.disable_csrf = True
        self.helper.form_id = 'property-details'
        self.fields['address_line_two'].required = False
        self.helper.layout = Layout(
            Div('property_type', css_class='col-md-6',
                style='padding-left: 0px'),
            Div('developer', css_class='col-md-6', style='padding-right:0px'),
            'address_line_one',
            'address_line_two',
            Div('city',
                'pin_code',
                'number_of_bathrooms',
                AppendedText('built_up_area', 'sq ft'),
                css_class='col-md-6',
                style='padding-left:0px'
                ),
            Div('state',
                'number_of_bedrooms',
                'number_of_parking_spaces',
                AppendedText('total_area', 'sq ft'),
                css_class='col-md-6',
                style='padding-right:0px'),

            'specifications',

            ButtonHolder(
                Submit('property-details', 'submit', css_class='btn-block',
                       css_id='submit-property-details')
            )
        )

    def save(self, commit=True):
        developer = self.cleaned_data['developer']
        developer, created = Developer.objects.get_or_create(name=developer)
        self.instance.developer = developer

        return super(PropertyForm, self).save()


class OtherDetailsForm(ModelForm):
    class Meta:
        model = Property
        fields = ['connectivity',
                  'neighborhood_quality',
                  'comments']

    def __init__(self, *args, **kwargs):
        super(OtherDetailsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields['connectivity'].required = False
        self.fields['neighborhood_quality'].required = False
        self.fields['comments'].required = False

        self.helper.layout = Layout(
            'connectivity',
            'neighborhood_quality',
            'comments',
            ButtonHolder(
                Submit('other-details', 'submit', css_class='btn-block',
                       css_id='submit-other-details')
            )
        )
