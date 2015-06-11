from django.views.generic import FormView
from braces import views
from django.http import HttpResponseRedirect

from forms import PropertyForm, OwnerForm, DeveloperProjectForm


class DeveloperProjectFormView(views.LoginRequiredMixin, FormView):
    form_class = DeveloperProjectForm
    template_name = 'new-property.html'
    success_url = 'success'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


class PropertyFormView(views.LoginRequiredMixin, FormView):
    form_class = PropertyForm
    template_name = 'new-property.html'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('success')


class OwnerFormView(FormView):
    form_class = OwnerForm
    template_name = 'new-property.html'