from crispy_forms.utils import render_crispy_form
from django.forms import inlineformset_factory
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
                   OtherDetailsForm,
                   DeveloperForm,
                   DeveloperProjectHelper, DeveloperProjectForm)
from properties.models import Property, Developer, DeveloperProject


class BasicDetailsFormView(views.LoginRequiredMixin, FormView):
    template_name = 'basic-details.html'
    form_class = PropertyBasicDetailsForm

    def get_form_kwargs(self):
        # Adding the request object to the form
        kwargs = {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
            'request': self.request,
        }
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def form_valid(self, form):
        property = form.save()
        return HttpResponseRedirect('/properties/dashboard/' + str(property.id))


DeveloperProjectFormset = inlineformset_factory(Developer, DeveloperProject,
                                                extra=1,
                                                form=DeveloperProjectForm, can_delete=False)

class DashboardView(views.LoginRequiredMixin, TemplateView):
    template_name = 'mega.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get(self, request, property_id, *args, **kwargs):
        p = Property.objects.get(id=property_id)
        property_form = PropertyForm(instance=p,
                                     initial={'developer': p.developer.name})
        owner_form = OwnerForm()
        # project_form and permission_form are art of a the same form
        project_form = ProjectForm()
        permission_form = PermissionForm()
        other_details_form = OtherDetailsForm(instance=p)
        builder_form = DeveloperForm(
            instance=Property.objects.get(id=property_id).developer
        )
        builder_project_formset = DeveloperProjectFormset(
            instance = Property.objects.get(id=property_id).developer
        )
        helper = DeveloperProjectHelper()

        forms = {
            'property_form': property_form,
            'owner_form': owner_form,
            'project_form': project_form,
            'permission_form': permission_form,
            'other_details_form': other_details_form,
            'builder_form': builder_form,
            'builder_project_formset': builder_project_formset,
            'helper': helper
        }

        return render(request, self.template_name, forms)

    def post(self, request, property_id, *args, **kwargs):
        print request.POST
        if request.is_ajax():

            property = Property.objects.get(id=property_id)
            property_form = PropertyForm(request.POST, instance=property)
            owner_form = OwnerForm(request.POST)
            project_form = ProjectForm(request.POST)
            permission_form = PermissionForm(request.POST)
            other_details_form = OtherDetailsForm(request.POST,
                                                  instance=property)
            builder_form = DeveloperForm(
                request.POST,
                instance=Property.objects.get(id=property_id).developer
            )
            builder_project_formset = DeveloperProjectFormset(
                request.POST,
                instance = Property.objects.get(id=property_id).developer
            )
            helper = DeveloperProjectHelper()

            if 'property-details' in request.POST:
                if property_form.is_valid():

                    property_form.save()
                    form_html = render_crispy_form(property_form)
                    return JsonResponse({'success': 'true',
                                         'form_html': form_html})
                else:
                    form_html = render_crispy_form(property_form)
                    return JsonResponse({'success': 'false',
                                         'form_html': form_html,
                                         'errors': property_form.errors})

            if 'owner-details' in request.POST:
                if owner_form.is_valid():
                    owner_form.save()
                    return JsonResponse({'success': 'true'})
                else:
                    form_html = render_crispy_form(owner_form)
                    return JsonResponse({'success': 'false',
                                         'form_html': form_html})

            if 'project-details' in request.POST:
                if project_form.is_valid() and permission_form.is_valid():
                    project = project_form.save()
                    permission_form.save(project=project)
                    return JsonResponse({'success': 'true'})
                else:
                    project_form_html = render_crispy_form(project_form)
                    permission_form_html = render_crispy_form(permission_form)
                    form_html = project_form_html + permission_form_html
                    return JsonResponse({'success': 'false',
                                         'form_html': form_html})

            if 'builder-details' in request.POST:
                if builder_form.is_valid() and builder_project_formset.is_valid():
                    builder_form.save()
                    builder_project_formset.save()
                    builder_form_html = render_crispy_form(builder_form)
                    builder_project_formset_html = render_crispy_form(
                        builder_project_formset, helper)
                    form_html = builder_form_html + builder_project_formset_html
                    return JsonResponse({'success': 'true',
                                         'form_html': form_html})
                else:
                    form_html = render_crispy_form(builder_form)
                    return JsonResponse({'success': 'false',
                                         'form_html': form_html})

            if 'other-details' in request.POST:
                if other_details_form.is_valid():
                    other_details_form.save()
                    form_html = render_crispy_form(other_details_form)
                    return JsonResponse({'success': 'true',
                                         'form_html': form_html})
                else:
                    form_html = render_crispy_form(other_details_form)
                    return JsonResponse({'success': 'true',
                                         'form_html': form_html})

            if 'add-project' in request.POST:
                print 'here'
                developer = Developer.objects.all().first()
                builder_form = DeveloperForm(initial = {'number_of_projects':request.POST['number_of_projects']})
                builder_form_html = render_crispy_form(builder_form)
                print request.POST['developerproject_set-TOTAL_FORMS']
                post_data = request.POST.copy()
                post_data['developerproject_set-TOTAL_FORMS'] = int(request.POST['developerproject_set-TOTAL_FORMS'])+1
                print post_data['developerproject_set-TOTAL_FORMS']
                builder_project_formset = DeveloperProjectFormset(post_data, instance=developer)
                helper = DeveloperProjectHelper()
                builder_project_formset_html = render_crispy_form(builder_project_formset, helper)
                form_html= builder_form_html+builder_project_formset_html
                print 'here2'

                return JsonResponse({'success':'true',
                                     'form_html':form_html})