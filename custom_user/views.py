from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import logout, authenticate, login
from django.views.generic import FormView, TemplateView, RedirectView
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from braces import views

from forms import RegistrationForm, LoginForm


class IndexView(views.LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class LogOutView(views.LoginRequiredMixin, RedirectView):
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)


class LoginView(views.AnonymousRequiredMixin, FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)
        else:
            return self.form_invalid(form)


class RegistrationView(views.AnonymousRequiredMixin, FormView):
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