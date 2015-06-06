from django.views.generic import FormView

from forms import RegistrationForm


class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'register.html'

    def form_valid(self, form):
        form.save()
