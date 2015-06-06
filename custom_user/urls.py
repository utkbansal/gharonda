from views import RegistrationView, LoginView

from django.conf.urls import url

urlpatterns = [
    url(r'^register/', RegistrationView.as_view(), name='register'),
    url(r'^login/', LoginView.as_view(), name='login'),
]