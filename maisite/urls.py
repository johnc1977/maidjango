from django.conf.urls import patterns, include, url
from mysite import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'maisite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^site/', include('mysite.urls')),
    url(r'^admin/', include(admin.site.urls)),    
)
