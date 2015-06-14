from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import FormView, TemplateView
from braces import views
from django.http import HttpResponseRedirect

from forms import PropertyForm, OwnerForm, DeveloperProjectForm, \
    ProjectBasicDetailsForm


class TestView(TemplateView):
    template_name = 'dashboard.html'


class BasicDetailsFormView(views.LoginRequiredMixin, FormView):
    # basic/
    template_name = 'new-property.html'
    form_class = ProjectBasicDetailsForm

    def form_valid(self, form):
        form_data = form.cleaned_data
        self.request.session['data'] = form_data
        return HttpResponseRedirect(reverse_lazy('new'))


class DeveloperProjectFormView(views.LoginRequiredMixin, FormView):
    form_class = DeveloperProjectForm
    template_name = 'new-property.html'
    success_url = 'success'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


class PropertyFormView(views.LoginRequiredMixin, FormView):
    # /new/
    form_class = PropertyForm
    template_name = 'new-property.html'

    def get(self, request, *args, **kwargs):
        if 'data' in request.session:
            initial = super(PropertyFormView, self).get_initial()
            initial['address_line_one'] = self.request.session['data'][
                'address_line_one']
            initial['address_line_two'] = self.request.session['data'][
                'address_line_two']
            initial['state'] = self.request.session['data']['state']
            initial['developer'] = self.request.session['data'][
                'developer_name']
            initial['pin_code'] = self.request.session['data']['pin_code']
            initial['city'] = self.request.session['data']['city']

            form = PropertyForm(initial=initial)

            self.request.session.pop('data')
            return self.render_to_response(self.get_context_data(form=form))

        messages.error(request, 'You need to add basic info first')
        return redirect(reverse_lazy('basic'))

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('success')


class OwnerFormView(FormView):
    form_class = OwnerForm
    template_name = 'new-property.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)
