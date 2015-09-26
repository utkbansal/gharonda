from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings

from custom_user.views import RegisterView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', RegisterView.as_view(), name='register'),
    url(r'', include('properties.urls')),
    url(r'^user/', include('custom_user.urls')),
    url(r'^ajaximage/', include('ajaximage.urls')),
]

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$',
                                'django.views.static.serve',
                                {'document_root': settings.MEDIA_ROOT, }),
                            )
