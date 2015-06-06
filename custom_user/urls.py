from views import RegistrationView

from django.conf.urls import include, url

urlpatterns = [
    url(r'^register/', RegistrationView.as_view(), name='register'),
]
