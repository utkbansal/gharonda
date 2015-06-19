from django.conf.urls import url

from views import (
    BasicDetailsFormView,
    DashboardView,
    DeveloperProjectFormView)

urlpatterns = [
    url(r'^project/$', DeveloperProjectFormView.as_view(), name='project'),
    url(r'^basic/$', BasicDetailsFormView.as_view(), name='basic'),
    url(r'^dashboard/(?P<property_id>[0-9]+)/$', DashboardView.as_view(),
        name='dashboard'),
    # url(r'^test/$', TestView.as_view(), name='test'),
]
