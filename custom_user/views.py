from django.views.generic import FormView
from django.http import HttpResponseRedirect

from django.contrib.auth import get_user_model

from forms import RegistrationForm, LoginForm


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'


class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = '/'

    def form_valid(self, form):
        get_user_model().objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['password'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            )
        return HttpResponseRedirect(self.get_success_url())