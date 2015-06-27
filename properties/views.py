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
                   DeveloperProjectHelper,
                   DeveloperProjectForm,
                   TowerHelper,
                   TowerForm)
from properties.models import (Property,
                               Developer,
                               DeveloperProject,
                               Project,
                               Tower,
                               ProjectPermission)


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
        self.request.session['owner_name'] = form.cleaned_data['owner_name']
        return HttpResponseRedirect('/properties/dashboard/' + str(property.id))


DeveloperProjectFormset = inlineformset_factory(Developer, DeveloperProject,
                                                extra=1,
                                                form=DeveloperProjectForm
                                                )

TowerFormset = inlineformset_factory(Project, Tower,
                                     form=TowerForm,
                                     extra=1,
                                     )


class DashboardView(views.LoginRequiredMixin, TemplateView):
    template_name = 'mega.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get(self, request, property_id, *args, **kwargs):
        p = Property.objects.get(id=property_id)
        project = p.project

        property_form = PropertyForm(instance=p,
                                     initial={'developer': p.developer.name}
                                     )

        # If the user is redirected from the basic details form, then initialise
        # the owner name from the basic details form
        if 'owner_name' in self.request.session:
            owner_form = OwnerForm(
                instance=p.owner,
                initial={
                    'name': self.request.session.pop('owner_name')
                }
            )

        # If the project doesn't have an owner, show empty form
        elif p.owner is None:
            owner_form = OwnerForm(instance=p.owner)

        # If the project has an owner, initialise with owner and co-owner
        # details
        else:
            owner_form = OwnerForm(
                instance=p.owner,
                initial={
                    'co_owner_name': p.owner.co_owner.name,
                    'co_owner_occupation': p.owner.co_owner.occupation,
                }
            )

        # project_form, permission_form and tower form comprise a single form
        # i.e. Project Details
        project_form = ProjectForm(instance=project)

        # Initialise permission form manually beacuse it cannot have an instance
        initial_permissions = {}
        for x in p.project.projectpermission_set.all():
            initial_permissions[x.permission.name]=x.value

        permission_form = PermissionForm(initial=initial_permissions)
        tower_form = TowerFormset(instance=project)
        tower_helper = TowerHelper()

        # builder_form and buider_project_formset comprise a single form
        builder_form = DeveloperForm(
            instance=Property.objects.get(id=property_id).developer
        )
        builder_project_formset = DeveloperProjectFormset(
            instance=Property.objects.get(id=property_id).developer
        )
        developer_project_helper = DeveloperProjectHelper()

        other_details_form = OtherDetailsForm(instance=p)

        forms = {
            'property_form': property_form,
            'owner_form': owner_form,
            'project_form': project_form,
            'permission_form': permission_form,
            'tower_form': tower_form,
            'tower_helper': tower_helper,
            'builder_form': builder_form,
            'builder_project_formset': builder_project_formset,
            'developer_project_helper': developer_project_helper,
            'other_details_form': other_details_form,
        }

        return render(request, self.template_name, forms)

    def post(self, request, property_id, *args, **kwargs):
        if request.is_ajax():

            property = Property.objects.get(id=property_id)

            property_form = PropertyForm(request.POST, instance=property)

            owner_form = OwnerForm(request.POST, instance=property.owner)

            project_form = ProjectForm(request.POST, instance=property.project)
            permission_form = PermissionForm(request.POST)
            tower_form = TowerFormset(request.POST,
                                      files=request.FILES,
                                      instance=property.project)
            tower_helper = TowerHelper()

            builder_form = DeveloperForm(
                request.POST,
                instance=Property.objects.get(id=property_id).developer
            )
            builder_project_formset = DeveloperProjectFormset(
                request.POST,
                instance=Property.objects.get(id=property_id).developer
            )
            developer_project_helper = DeveloperProjectHelper()

            other_details_form = OtherDetailsForm(request.POST,
                                                  instance=property)

            if 'property-details' in request.POST:
                if property_form.is_valid():

                    property_form.save()
                    form_html = render_crispy_form(property_form)
                    return JsonResponse({'success': 'true',
                                         'form_html': form_html})
                else:
                    form_html = render_crispy_form(property_form)
                    return JsonResponse({'success': 'false',
                                         'form_html': form_html})

            if 'owner-details' in request.POST:
                if owner_form.is_valid():
                    owner_form.save(property_id)
                    form_html = render_crispy_form(owner_form)
                    return JsonResponse({'success': 'true',
                                         'form_html': form_html})
                else:
                    form_html = render_crispy_form(owner_form)
                    return JsonResponse({'success': 'false',
                                         'form_html': form_html})

            if 'project-details' in request.POST:
                if project_form.is_valid() and permission_form.is_valid() and \
                        tower_form.is_valid():
                    project = project_form.save(property_id)
                    permission_form.save(project=project)
                    tower_form.save()

                    project_form_html = render_crispy_form(project_form)
                    permission_form_html = render_crispy_form(permission_form)
                    tower_form_html = render_crispy_form(tower_form, tower_helper)

                    form_html = (project_form_html +
                                 permission_form_html +
                                 tower_form_html)


                    return JsonResponse({'success': 'true',
                                         'form_html':form_html})
                else:
                    project_form_html = render_crispy_form(project_form)
                    permission_form_html = render_crispy_form(permission_form)
                    tower_form_html = render_crispy_form(tower_form,
                                                         tower_helper)
                    form_html = (project_form_html +
                                 permission_form_html +
                                 tower_form_html)
                    return JsonResponse({'success': 'false',
                                         'form_html': form_html})

            if 'builder-details' in request.POST:
                if builder_form.is_valid() and \
                        builder_project_formset.is_valid():
                    builder_form.save()
                    builder_project_formset.save()
                    builder_form_html = render_crispy_form(builder_form)
                    builder_project_formset_html = render_crispy_form(
                        builder_project_formset, developer_project_helper)
                    form_html = builder_form_html + builder_project_formset_html
                    return JsonResponse({'success': 'true',
                                         'form_html': form_html})
                else:
                    form_html = render_crispy_form(builder_form)
                    return JsonResponse({'success': 'false',
                                         'form_html': form_html})

            if 'add-tower' in request.POST:
                post_data = request.POST.copy()
                post_data['tower_set-TOTAL_FORMS'] = int(
                    request.POST['tower_set-TOTAL_FORMS']) + 1

                project = Property.objects.get(id=property_id).project
                tower_form = TowerFormset(post_data, instance=project)

                tower_helper = TowerHelper()
                tower_form_html = render_crispy_form(tower_form, tower_helper)
                print tower_form.errors

                form_html = tower_form_html

                return JsonResponse({'succcess': 'true',
                                     'form_html': form_html})

            if 'add-project' in request.POST:
                developer = Developer.objects.all().first()
                builder_form = DeveloperForm(
                    initial={
                        'number_of_projects': request.POST['number_of_projects']
                    }
                )
                builder_form_html = render_crispy_form(builder_form)
                post_data = request.POST.copy()
                post_data['developerproject_set-TOTAL_FORMS'] = int(
                    request.POST['developerproject_set-TOTAL_FORMS']) + 1
                builder_project_formset = DeveloperProjectFormset(
                    post_data,
                    instance=developer
                )

                developer_project_helper = DeveloperProjectHelper()
                builder_project_formset_html = render_crispy_form(
                    builder_project_formset, developer_project_helper)
                form_html = builder_form_html + builder_project_formset_html

                return JsonResponse({'success': 'true',
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
