from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PVPS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^show_2016/', include( 'show_2016.urls')),
    url(r'^admin/', include(admin.site.urls)),
        
)
