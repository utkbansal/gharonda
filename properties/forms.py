from crispy_forms.bootstrap import AppendedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from django.forms import ModelForm
from django import forms

from models import Property, Owner, Developer, DeveloperProjects


class ProjectBasicDetailsForm(forms.Form):
    name = forms.CharField()
    developer_name = forms.CharField()
    address_line_one = forms.CharField()
    address_line_two = forms.CharField(required=False)
    state = forms.CharField()
    pin_code = forms.IntegerField()
    owner_name = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(ProjectBasicDetailsForm, self).__init__(*args, **kwargs )
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'developer_name',
            'address_line_one',
            'address_line_two',
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

    def __init__(self, *args, **kwargs):
        super(OwnerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'occupation',
            'co_owner_name',
            'co_owner_occupation',
            'pan_number',
            'date_of_purchase',
            'loan_from',
            'cost_of_purchase',
            'is_resale',
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

        co_owner, created = Owner.objects.get_or_create(name=co_owner_name,
                                                        occupation=co_owner_occupation)

        self.instance.co_owner = co_owner

        return super(OwnerForm, self).save()


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
                choices=((1, 1,), (2, 2), (3, 3)), ),
            'number_of_bathrooms': forms.Select(
                choices=((1, 1,), (2, 2), (3, 3)), ),
            'number_of_parking_spaces': forms.Select(
                choices=((1, 1,), (2, 2), (3, 3)), ),
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
