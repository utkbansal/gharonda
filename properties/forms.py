from crispy_forms.bootstrap import AppendedText, InlineRadios, \
    PrependedAppendedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Field, Div, \
    Fieldset
from django.forms import ModelForm
from django import forms

from models import (Property,
                    Owner,
                    Developer,
                    DeveloperProject,
                    Project, ProjectPermission,
                    Bank,
                    Permissions,
                    Tower, City, State, PinCode)

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


class SearchForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all())
    project = forms.IntegerField(widget=forms.Select)
    rent_or_sale = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=(('rent', 'For Rent'), ('sale', 'For Sale')),
        label=''
    )

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.disable_csrf = True

        self.helper.layout = Layout(
            'city',
            'project',
            InlineRadios('rent_or_sale'),
            ButtonHolder(
                Submit('submit', 'Search', css_class='btn-primary btn-block')
            )
        )


class DeveloperForm(ModelForm):
    class Meta:
        model = Developer
        fields = ['number_of_projects',
                  'developer_report'
                  ]

        widgets = {
            'developer_report': forms.Select(choices=(('Great', 'Great'),
                                                      ('OK', 'OK'),
                                                      ('Bad', 'Bad'))),
            'number_of_projects': forms.NumberInput(attrs={'min': 0})
        }

    def __init__(self, *args, **kwargs):
        super(DeveloperForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.disable_csrf = True
        self.helper.form_tag = False
        self.fields['developer_report'].required = False
        self.fields['number_of_projects'].required = False


class DeveloperProjectHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(DeveloperProjectHelper, self).__init__(*args, **kwargs)
        self.form_tag = False
        self.add_input(
            Submit("add-project", "Add Project", css_class='btn-block',
                   css_id='add-project'))
        self.add_input(Submit("builder-details", "Save", css_class='btn-block',
                              css_id='submit-builder-details'))
        self.disable_csrf = True
        self.layout = Layout(
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

            Div(
                Field('other_status'),
                css_class='col-md-12',
                style='padding:0px',
            ),
            Div(
                Field('status'),
                css_class='col-md-12',
                style='padding:0px',
            ),
            Div(
                Field('address'),
                css_class='col-md-12',
                style='padding:0px',
            ),

            Div(
                'DELETE',
                css_class='col-md-12',
                style='padding:0px',
            ),
            'developer',
        )


class DeveloperProjectForm(ModelForm):
    developer = forms.CharField()

    class Meta:
        model = DeveloperProject
        fields = [
            'project_name',
            'launch_date',
            'possession_date',
            'address',
            'status',
            'other_status'
        ]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 5}),
            'other_status': forms.Textarea(attrs={'rows': 5}),
            'status': forms.Select(choices=(
                # Blank field so that DeveloperProject isn't saved when the
                #  status isn't changed
                ('', '--------'),
                ('Completed', 'Completed'),
                ('Under Construction', 'Under Construction'),
                ('Project Announced', 'Project Announced'),
            ))
        }

        labels = {
            'other_status': 'Comment'
        }

    def __init__(self, *args, **kwargs):
        super(DeveloperProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.disable_csrf = True
        self.helper.form_id = 'builder-details'
        self.fields['project_name'].required = False
        self.fields['launch_date'].required = False
        self.fields['possession_date'].required = False
        self.fields['other_status'].required = False
        self.fields['status'].required = False
        self.fields['address'].required = False
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
            'status',
            'address',
            'developer',
        )

    def save(self, commit=True):
        developer = self.cleaned_data['developer']
        developer, created = Developer.objects.get_or_create(name=developer)
        self.instance.developer = developer

        return super(DeveloperProjectForm, self).save()


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
        self.helper.disable_csrf = True
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


class OwnerForm(ModelForm):
    co_owner_name = forms.CharField(required=False)
    co_owner_occupation = forms.CharField(required=False)

    class Meta:
        model = Owner
        fields = [
            'name',
            'occupation',
            'pan_number',
            'date_of_purchase',
            'date_of_sale',
            'loan_status',
            'loan_from',
            'main_cost_of_purchase',
            'is_resale',
            'name_of_seller',
            'contact_number_seller',
            'email_seller',
            'other_cost_1',
            'other_cost_2',
            'other_cost_3',
        ]

        widgets = {
            'is_resale': forms.RadioSelect,
        }

        labels = {
            'is_resale': 'Property for resale',
            'main_cost_of_purchase': 'Basic cost of purchase',
            'loan_status': 'Loan on property',
            'other_cost_1': 'EDC',
            'other_cost_2': 'IDC',
            'other_cost_3': 'Parking',
        }

    def __init__(self, *args, **kwargs):
        super(OwnerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_id = 'owner-form'
        self.helper.disable_csrf = True
        self.fields['name_of_seller'].required = False
        self.fields['occupation'].required = False
        self.fields['pan_number'].required = False
        self.fields['contact_number_seller'].required = False
        self.fields['email_seller'].required = False
        self.fields['loan_from'].required = False
        self.fields['main_cost_of_purchase'].required = False
        self.fields['date_of_sale'].required = False
        self.fields['other_cost_1'].required = False
        self.fields['other_cost_2'].required = False
        self.fields['other_cost_3'].required = False
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('name',
                        'occupation',
                        'pan_number',
                        Field('date_of_purchase', css_class='month-year'),
                        css_class='col-md-6',
                        style='padding-left:0px'),

                    Div(
                        'co_owner_name',
                        'co_owner_occupation',
                        # Indian rupee sign &#8377;
                        PrependedAppendedText('main_cost_of_purchase',
                                              '&#8377;',
                                              'per sq ft'),
                        Field('date_of_sale', css_class='month-year'),

                        css_class='col-md-6',
                        style='padding-right:0px'
                    ),
                ),

                Div(
                    'loan_status',
                    'loan_from',
                    css_class='col-md-12',
                    style='padding:0px'
                ),

                Div(
                    Fieldset(
                        'Other Costs',
                        Div(
                            PrependedAppendedText('other_cost_1', '&#8377;',
                                                  'per sq ft'),
                            PrependedAppendedText('other_cost_3', '&#8377;',
                                                  'per sq ft'),
                            css_class='col-md-6',
                            style='padding-left:0px'
                        ),
                        Div(
                            PrependedAppendedText('other_cost_2', '&#8377;',
                                                  'per sq ft'),
                            css_class='col-md-6',
                            style='padding-right:0px'
                        ),
                    ),
                    css_class='col-md-12',
                    style='padding:0px',
                ),
                Div(
                    InlineRadios('is_resale'),
                    css_class='col-md-12',
                    style='padding:0px'
                ),

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
                Div(
                    'email_seller',
                    css_class='col-md-12',
                    style='padding:0px',
                ),
                ButtonHolder(
                    Submit('owner-details', 'submit', css_class='btn-block',
                           css_id='submit-owner-details')

                )
            )
        )

    def save(self, property_id, commit=True):
        co_owner_name = self.cleaned_data['co_owner_name']
        co_owner_occupation = self.cleaned_data['co_owner_occupation']

        co_owner, created = Owner.objects.get_or_create(
            name=co_owner_name,
            occupation=co_owner_occupation
        )

        self.instance.co_owner = co_owner

        property = Property.objects.get(id=property_id)

        owner = super(OwnerForm, self).save()

        property.owner = owner
        property.save()
        return owner


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
            self.fields[permission.name + '_comment'] = forms.CharField()

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.form_id = 'permission-form'

    def save(self, *args, **kwargs):
        project = kwargs.pop('project')
        for field in self.fields:
            permission = Permissions.objects.filter(name=field).first()

            if permission is not None:
                print self.cleaned_data[field + '_comment']

                p = ProjectPermission.objects.update_or_create(
                    project=project,
                    permission=permission,
                    defaults={
                        'value': self.cleaned_data[field],
                        'comment': self.cleaned_data[field + '_comment']

                    })
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
            'status',
            'permit_report'
        ]

        labels = {
            'bank': 'Banks Providing Loans For The Project',
            'status': 'Project Status',
            'permit_report': 'Permit Status'
        }

        widgets = {
            'status': forms.Select(
                choices=(
                    ('On Track', 'On Track'),
                    ('Lagging', 'Lagging'),
                    ('Stay Away', 'Stay Away')
                )
            ),
            'permit_report': forms.Select(
                choices=(
                    ('Meets', 'Meets'),
                    ('On Track', 'On Track'),
                    ('Does Not', 'Does Not')
                )
            )
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_id = 'project-form'
        self.helper.disable_csrf = True
        self.fields['bank'].required = False
        self.fields['contractor_name_1'].required = False
        self.fields['contractor_name_2'].required = False
        self.fields['contractor_name_3'].required = False
        self.helper.layout = Layout(
            'name',
            Div(
                Field('launch_date', css_class='month-year'),
                css_class='col-md-6',
                style='padding-left:0px'
            ),
            Div(
                Field('possession_date',
                      css_class='month-year',
                      ),
                css_class='col-md-6',

                style='padding-right:0px'),
            'bank',
            'add_bank',
            'new_bank',
            'contractor_name_1',
            'contractor_name_2',
            'contractor_name_3',
            'status'
        )

    def save(self, property_id, commit=True):
        property = Property.objects.get(id=property_id)
        if 'add_bank' in self.cleaned_data.keys():
            if self.cleaned_data['add_bank'] is True:
                bank = Bank(name=self.cleaned_data['new_bank'])

                project = super(ProjectForm, self).save()
                bank.save()
                project.bank.add(bank)

                property.project = project
                property.save()
                return project

        project = super(ProjectForm, self).save()
        property.project = project
        property.save()
        return project


class PropertyBasicDetailsForm(ModelForm):
    developer_name = forms.CharField()
    project_name = forms.CharField()
    owner_name = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    pin_code = forms.IntegerField()

    class Meta:
        model = Property
        fields = [
            'address_line_one',
            'address_line_two',

        ]

        widgets = {
            'city': forms.TextInput(),
            'state': forms.TextInput(),
            'pin_code': forms.TextInput(),

        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(PropertyBasicDetailsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'project-basic-details-form'
        self.fields['address_line_two'].required = False
        self.fields['state'].required = False
        self.fields['pin_code'].required = False
        self.helper.layout = Layout(
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

        project_name = self.cleaned_data['project_name']
        project, created = Project.objects.get_or_create(name=project_name)
        self.instance.created_by = self.request.user
        self.instance.project = project

        city_name = self.cleaned_data['city'].title()
        city, created = City.objects.get_or_create(name=city_name)
        self.instance.city = city

        state_name = self.cleaned_data['state'].title()
        if state_name != '':
            state, created = State.objects.get_or_create(name=state_name)
            self.instance.state = state

        pin_code = self.cleaned_data['pin_code']
        if pin_code != None:
            pin_code, created = PinCode.objects.get_or_create(code=pin_code)

            self.instance.pin_code = pin_code

        return super(PropertyBasicDetailsForm, self).save()


class PropertyForm(ModelForm):
    developer = forms.CharField(label='Builder Name')
    city = forms.CharField()
    state = forms.CharField()
    pin_code = forms.IntegerField()

    class Meta:
        model = Property
        fields = [
            'property_type',
            'specifications',
            'plot_area',
            'total_area',
            'number_of_bedrooms',
            'number_of_bathrooms',
            'number_of_parking_spaces',
            'address_line_one',
            'address_line_two',
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
            'specifications': forms.Select(choices=SPECIFICATION_CHOICE),
            'plot_area': forms.NumberInput(attrs={'min': 0}),
            'total_area': forms.NumberInput(attrs={'min': 0}),
        }

    def __init__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.disable_csrf = True
        self.helper.form_id = 'property-details'
        self.fields['address_line_two'].required = False
        self.fields['state'].required = False
        self.fields['pin_code'].required = False
        self.fields['number_of_bedrooms'].required = False
        self.fields['number_of_bathrooms'].required = False
        self.fields['number_of_parking_spaces'].required = False
        self.fields['total_area'].required = False
        self.helper.layout = Layout(
            Div('property_type', css_class='col-md-6',
                style='padding-left: 0px'),
            Div('developer', css_class='col-md-6', style='padding-right:0px'),
            'address_line_one',
            'address_line_two',
            Div(
                'city',
                'pin_code',
                'number_of_bathrooms',
                AppendedText('plot_area', 'sq ft'),
                css_class='col-md-6',
                style='padding-left:0px'
            ),
            Div(
                'state',
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

        city_name = self.cleaned_data['city'].title()
        city, created = City.objects.get_or_create(name=city_name)
        self.instance.city = city

        state_name = self.cleaned_data['state'].title()
        state, created = State.objects.get_or_create(name=state_name)

        self.instance.state = state

        pin_code = self.cleaned_data['pin_code']
        pin_code, created = PinCode.objects.get_or_create(code=pin_code)
        self.instance.pin_code = pin_code

        return super(PropertyForm, self).save()


class TowerForm(ModelForm):
    class Meta:
        model = Tower
        fields = ['name',
                  'floors_completed',
                  'finishing_status',
                  'other_status',
                  'image'
                  ]

        widgets = {
            'floors_completed': forms.NumberInput(attrs={'min': 0})
        }

    def __init__(self, *args, **kwargs):
        super(TowerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.fields['name'].required = False
        self.fields['floors_completed'].required = False
        self.fields['finishing_status'].required = False
        self.fields['other_status'].required = False
        self.fields['image'].required = False


class TowerHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(TowerHelper, self).__init__(*args, **kwargs)
        self.form_tag = False
        self.add_input(
            Submit("add-tower", "Add Tower", css_class='btn-block',
                   css_id='add-tower'))
        self.add_input(
            Submit('project-details', 'Submit', css_class='btn-block',
                   css_id='submit-project-details')
        )
        self.disable_csrf = True
        self.layout = Layout(
            Fieldset(
                'Tower Info',
                Div(
                    'name',
                    css_class='col-md-6',
                    style='padding-left:0px'),
                Div(
                    'floors_completed',
                    css_class='col-md-6',
                    style='padding-right:0px'),
                Div('finishing_status',
                    'other_status',
                    css_class='col-md-12',
                    style='padding:0px'),
                Div(
                    'image',
                    css_class='col-md-12',
                    style='padding:0% 0% 5% 0%'
                ))
        )
        self.layout.extend(['DELETE'])
