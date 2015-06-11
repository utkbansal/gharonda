from django.conf.urls import url

from views import PropertyFormView, OwnerFormView

urlpatterns = [
    url(r'^new/$', PropertyFormView.as_view(), name='new'),
    url(r'^owner/$', OwnerFormView.as_view(), name='owner'),

]