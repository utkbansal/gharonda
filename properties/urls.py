from django.conf.urls import url

from views import PropertyFormView, OwnerFormView, DeveloperProjectFormView

urlpatterns = [
    url(r'^new/$', PropertyFormView.as_view(), name='new'),
    url(r'^owner/$', OwnerFormView.as_view(), name='owner'),
    url(r'^project/$', DeveloperProjectFormView.as_view(), name='project'),
]