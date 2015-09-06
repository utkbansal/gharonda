from crispy_forms.bootstrap import InlineRadios
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django import forms

from models import BrokerProfile, Company, ContactNumber


class BrokerProfileForm(ModelForm):
    class Meta:
        model = BrokerProfile
        fields = ['license_no']
        widgets = {
            'license_no': forms.TextInput(),
            # 'company': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super(BrokerProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf=True
        self.fields['license_no'].required = False


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address']

        labels = {
            'name': 'Company Name'
        }

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['address'].required = False
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            'name',
            'address'
        )


class ContactNumberForm(ModelForm):
    class Meta:
        model = ContactNumber
        fields = ['contact_no']

    def __init__(self, *args, **kwargs):
        super(ContactNumberForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            'contact_no',
        )


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.attrs = {'name': 'registration-form'}
        self.helper.layout = Layout(
            'username',
            'password',
        )


class RegistrationForm(ModelForm):
    # password2 = forms.CharField(widget=forms.PasswordInput(),
    # required=True,
    # label='Confirm Password')

    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.disable_csrf = True
        # Removing the enclosing <form> tag
        self.helper.form_tag = False
        self.helper.attrs = {'name': 'registration-form'}
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'email',
            'password',
        )


CHOICES = (('broker', 'Broker',), ('normal-user', 'Consumer',))


class UserTypeForm(forms.Form):
    # Not a crispy form
    type = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    def __init__(self, *args, **kwargs):
        super(UserTypeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.disable_csrf = True
        self.helper.form_tag = False
        self.helper.attrs = {
            'name': 'user-type-form',
            'onsubmit': 'return ShowNextForm()',
        }
        # self.fields['type'].attrs = {'onclick':'fieldVisiblityCheck()'}
        self.helper.layout = Layout(
            InlineRadios('type'),
        )
