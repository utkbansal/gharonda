from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import logout, authenticate, login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, TemplateView, RedirectView
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from braces import views
from django.shortcuts import render, redirect

from forms import (RegistrationForm,
                   LoginForm,
                   UserTypeForm,
                   BrokerProfileForm,
                   CompanyForm,
                   ContactNumberForm)
from models import BrokerProfile, User, Company, ContactNumber


class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        contact_form = ContactNumberForm(instance=ContactNumber())
        company_form = CompanyForm(instance=Company())
        register_form = RegistrationForm(instance=User())
        broker_profile_form = BrokerProfileForm(instance=BrokerProfile())
        user_type_form = UserTypeForm()

        if self.request.user.is_authenticated():
            return redirect(reverse_lazy('search'))

        return render(request, self.template_name,
                      {'user_type_form': user_type_form,
                       'register_form': register_form,
                       'broker_profile_form': broker_profile_form,
                       'company_form': company_form,
                       'contact_form': contact_form,
                      }
        )

    def post(self, request, *args, **kwargs):
        register_form = RegistrationForm(request.POST, instance=User())
        broker_profile_form = BrokerProfileForm(request.POST,
                                                instance=BrokerProfile())
        user_type_form = UserTypeForm(request.POST)
        contact_form = ContactNumberForm(request.POST, instance=ContactNumber())
        company_form = CompanyForm(request.POST, instance=Company())

        forms = {
            'user_type_form': user_type_form,
            'register_form': register_form,
            'broker_profile_form': broker_profile_form,
            'company_form': company_form,
            'contact_form': contact_form,
        }

        if user_type_form.is_valid():
            if register_form.is_valid():
                user = get_user_model().objects.create_user(
                    register_form.cleaned_data['email'],
                    register_form.cleaned_data['password'],
                    first_name=register_form.cleaned_data['first_name'],
                    last_name=register_form.cleaned_data['last_name'],
                )

                if user_type_form.cleaned_data['type'] == 'normal-user':
                    user = authenticate(username=user.email,
                                        password=register_form.cleaned_data[
                                            'password'])
                    print 'logging in'
                    login(self.request, user)
                    print 'logged in'
                    return redirect(reverse_lazy('index'))

                if company_form.is_valid():
                    company, created = Company.objects.get_or_create(
                        name=company_form.cleaned_data['name'],
                        address=company_form.cleaned_data['address']
                    )
                    if broker_profile_form.is_valid():
                        BrokerProfile(
                            license_no=broker_profile_form.cleaned_data[
                                'license_no'],
                            user=user,
                            company=company,
                        ).save()
                    else:
                        user.delete()
                        return render(request, self.template_name, forms)

                else:
                    user.delete()
                    return render(request, self.template_name, forms)

                if contact_form.is_valid():
                    ContactNumber.objects.create(
                        contact_no=contact_form.cleaned_data['contact_no'],
                        user=user)
                else:
                    user.delete()
                    return render(request, self.template_name, forms)

            else:
                return render(request, self.template_name, forms)

        else:
            return render(request, self.template_name, forms)
        user = authenticate(username=register_form.cleaned_data['email'],
                            password=register_form.cleaned_data['password'])
        login(self.request, user)
        return HttpResponseRedirect(reverse_lazy('index'))


class LogOutView(views.LoginRequiredMixin, RedirectView):
    url = reverse_lazy('index')

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
