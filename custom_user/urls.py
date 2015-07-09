from django.conf.urls import url

from views import LoginView, IndexView, LogOutView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogOutView.as_view(), name='logout'),
]