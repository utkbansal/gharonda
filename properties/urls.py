from django.conf.urls import url

from views import (
    BasicDetailsFormView,
    DashboardView,
    SearchView,
    city_filter,
    PropertyDetailView,
    PropertyListView)

urlpatterns = [
    url(r'^basic/$', BasicDetailsFormView.as_view(), name='basic'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^property/(?P<city_slug>[\w-]+)/(?P<project_id>[0-9]+)/$',
        PropertyListView.as_view(), name='property-list'),
    url(r'^property/(?P<pk>[0-9]+)/$', PropertyDetailView.as_view(),
        name='property-detail'),
    url(r'^dashboard/property_filter/$', city_filter, name='city-filter'),
    url(r'^dashboard/(?P<property_id>[0-9]+)/$', DashboardView.as_view(),
        name='dashboard'),
]
