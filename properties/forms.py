from crispy_forms.bootstrap import AppendedText

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Button
from django.forms import ModelForm
from django import forms

from models import Property, Owner, Developer, DeveloperProjects


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
        self.helper.add_input(
            Button('back', "Back", css_class='btn btn-primary btn-block '))


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
