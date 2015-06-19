from crispy_forms.utils import render_crispy_form
# from django.core.serializers import json
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, TemplateView
from braces import views
from django.http import HttpResponseRedirect, JsonResponse

from forms import (PropertyForm,
                   OwnerForm,
                   PropertyBasicDetailsForm,
                   ProjectForm,
                   PermissionForm,
                   OtherDetailsForm, DeveloperProjectForm)
from properties.models import Property


class BasicDetailsFormView(views.LoginRequiredMixin, FormView):
    template_name = 'basic-details.html'
    form_class = PropertyBasicDetailsForm

    def form_valid(self, form):
        print self.request.POST
        property = form.save()
        # self.request.session
        return HttpResponseRedirect('/properties/dashboard/' + str(property.id))


class DashboardView(views.LoginRequiredMixin, TemplateView):
    template_name = 'mega.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get(self, request, property_id, *args, **kwargs):
        print property_id
        p = Property.objects.get(id=property_id)
        property_form = PropertyForm(instance=p,
                                     initial={'developer': p.developer.name})
        owner_form = OwnerForm()
        # project_form and permission_form are art of a the same form
        project_form = ProjectForm()
        permission_form = PermissionForm()
        other_details_form = OtherDetailsForm(instance=p)

        forms = {
            'property_form': property_form,
            'owner_form': owner_form,
            'project_form': project_form,
            'permission_form': permission_form,
            'other_details_form': other_details_form
        }

        return render(request, self.template_name, forms)

    def post(self, request, property_id, *args, **kwargs):
        if request.is_ajax():

            property = Property.objects.get(id=property_id)
            property_form = PropertyForm(request.POST, instance=property)
            owner_form = OwnerForm(request.POST)
            project_form = ProjectForm(request.POST)
            permission_form = PermissionForm(request.POST)
            other_details_form = OtherDetailsForm(request.POST,
                                                  instance=property)
            print request.POST
            if 'property-details' in request.POST:
                if property_form.is_valid():

                    property_form.save()
                    form_html = render_crispy_form(property_form)
                    # data = {'success': 'test'}
                    # return  HttpResponse(json.dumps(data), content_type='application/json')
                    return JsonResponse({'success': 'true',
                                         'form_html': form_html})
                else:
                    form_html = render_crispy_form(property_form)
                    return JsonResponse({'success': 'false',
                                         'form_html': form_html,
                                         'errors': property_form.errors})

            if 'owner-details' in request.POST:
                if owner_form.is_valid():
                    print request.POST
                    print 'owner form valid'
                    owner_form.save()
                    return JsonResponse({'success': 'true'})
                else:
                    form_html = render_crispy_form(owner_form)
                    return JsonResponse({'success': 'false',
                                         'form_html': form_html})

            if 'project-details' in request.POST:
                if project_form.is_valid() and permission_form.is_valid():
                    print 'valid project form'
                    project = project_form.save()
                    permission_form.save(project=project)
                    return JsonResponse({'success': 'true'})
                else:
                    project_form_html = render_crispy_form(project_form)
                    permission_form_html = render_crispy_form(permission_form)
                    form_html = project_form_html + permission_form_html
                    return JsonResponse({'success': 'false',
                                         'form_html': form_html})

            if 'other-details' in request.POST:
                if other_details_form.is_valid():
                    print 'other details form submitted'
                    other_details_form.save()
                    form_html = render_crispy_form(other_details_form)
                    return JsonResponse({'success': 'true',
                                         'form_html': form_html})
                else:
                    form_html = render_crispy_form(other_details_form)
                    return JsonResponse({'success': 'true',
                                         'form_html': form_html})


class DeveloperProjectFormView(views.LoginRequiredMixin, FormView):
    form_class = DeveloperProjectForm
    template_name = 'new-property.html'
    success_url = 'success'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)
