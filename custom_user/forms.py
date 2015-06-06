from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):

        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs = {'name': 'registration-form'}
        self.helper.layout = Layout(
            'username',
            'password',
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn-block ')
            ),
        )


class RegistrationForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
        ]

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.attrs = {'name': 'registration-form'}
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'email',
            'password',
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn-block ')
            ),
        )