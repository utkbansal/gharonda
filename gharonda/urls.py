from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('custom_user.urls')),
    url(r'^properties/', include('properties.urls')),
    url(r'^ajaximage/', include('ajaximage.urls')),
]

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$',
                                'django.views.static.serve',
                                {'document_root': settings.MEDIA_ROOT, }),
                            )
