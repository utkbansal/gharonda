from django.conf.urls import url

from views import LoginView, RegisterView, LogOutView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^logout/$', LogOutView.as_view(), name='logout'),
]