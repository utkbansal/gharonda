from crispy_forms.bootstrap import AppendedText, InlineRadios
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from django.forms import ModelForm
from django import forms

from models import Property, Owner, Developer, DeveloperProjects, Project, \
    ProjectPermission, Bank, Permissions


class PermissionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PermissionForm, self).__init__(*args, **kwargs)

        permissions = Permissions.objects.all()
        for permission in permissions:
            self.fields[permission.name] = forms.CharField()

        self.helper = FormHelper()
        self.helper.form_tag = False

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
            'new_bank'
        ]

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields['bank'].required = False
        self.helper.layout = Layout(
            'name',
            'launch_date',
            'possession_date',
            'bank',
            'add_bank',
            'new_bank',
            # ButtonHolder(
            #     Submit('Submit', 'submit', css_class='btn-block')
            # )
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


class ProjectBasicDetailsForm(forms.Form):
    name = forms.CharField()
    developer_name = forms.CharField()
    address_line_one = forms.CharField()
    address_line_two = forms.CharField(required=False)
    city = forms.CharField()
    state = forms.CharField()
    pin_code = forms.CharField()
    owner_name = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(ProjectBasicDetailsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'developer_name',
            'address_line_one',
            'address_line_two',
            'city',
            'state',
            'pin_code',
            'owner_name',
            ButtonHolder(
                Submit('Submit', 'submit', css_class='btn-block')
            )
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


class DeveloperProjectForm(ModelForm):
    developer = forms.CharField()

    class Meta:
        model = DeveloperProjects
        fields = [
            'project_name',
            'launch_date_month',
            'launch_date_year',
            'possession_date_month',
            'possession_date_year',
        ]
        widgets = {
            'launch_date_month': forms.Select(choices=MONTHS),
            'possession_date_month': forms.Select(choices=MONTHS),
        }

    def __init__(self, *args, **kwargs):
        super(DeveloperProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'project_name',
            'launch_date_month',
            'launch_date_year',
            'possession_date_month',
            'possession_date_year',
            'developer',
            ButtonHolder(
                Submit('Submit', 'submit', css_class='btn-block')
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
        self.fields['name_of_seller'].required = False
        self.fields['contact_number_seller'].required = False
        self.fields['email_seller'].required = False
        self.helper.layout = Layout(
            'name',
            'occupation',
            'co_owner_name',
            'co_owner_occupation',
            'pan_number',
            'date_of_purchase',
            'loan_from',
            'cost_of_purchase',
            InlineRadios('is_resale'),
            'name_of_seller',
            'contact_number_seller',
            'email_seller',
            ButtonHolder(
                Submit('Submit', 'submit', css_class='btn-block')
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


class PropertyForm(ModelForm):
    developer = forms.CharField()

    class Meta:
        model = Property
        fields = [
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
        }

    def __init__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['address_line_two'].required = False,
        self.helper.layout = Layout(
            AppendedText('built_up_area', 'sq ft'),
            AppendedText('total_area', 'sq ft'),
            'number_of_bedrooms',
            'number_of_bathrooms',
            'number_of_parking_spaces',
            'address_line_one',
            'address_line_two',
            'city',
            'state',
            'pin_code',
            'developer',
            ButtonHolder(
                Submit('Submit', 'submit', css_class='btn-block')
            )
        )

    def save(self, commit=True):
        developer = self.cleaned_data['developer']
        developer, created = Developer.objects.get_or_create(name=developer)
        self.instance.developer = developer

        return super(PropertyForm, self).save()
