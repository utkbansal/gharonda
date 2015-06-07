from django.conf.urls import url

from views import RegistrationView, LoginView, IndexView, LogOutView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^register/$', RegistrationView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogOutView.as_view(), name='logout'),
]