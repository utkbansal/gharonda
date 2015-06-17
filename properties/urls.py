from django.conf.urls import url

from views import PropertyFormView, OwnerFormView, DeveloperProjectFormView, \
    BasicDetailsFormView, ProjectView

urlpatterns = [
    url(r'^new/$', PropertyFormView.as_view(), name='new'),
    url(r'^owner/$', OwnerFormView.as_view(), name='owner'),
    url(r'^project/$', DeveloperProjectFormView.as_view(), name='project'),
    # url(r'^test/$', TestView.as_view(), name='test'),
    url(r'^basic/$', BasicDetailsFormView.as_view(), name='basic'),
    url(r'^any/$', ProjectView.as_view(), name='any'),
]
