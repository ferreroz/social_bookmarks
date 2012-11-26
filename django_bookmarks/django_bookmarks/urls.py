import os.path
from django.conf.urls import *
from bookmarks.views import *
site_media = os.path.join(
    os.path.dirname(__file__), 'site_media'
)
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
  # Browing
  (r'^$', main_page),
  (r'^user/(\w+)/$', user_page),
  
  # Session management
  (r'^login/$', 'django.contrib.auth.views.login'),
  (r'^logout/$', logout_page),
  (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': site_media}),
  (r'^register/$', register_page),
    # Examples:
    # url(r'^$', 'django_bookmarks.views.home', name='home'),
    # url(r'^django_bookmarks/', include('django_bookmarks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
  (r'^register/success/$', direct_to_template, {'template': 'registration/register_success.html'}),
  
  # Account management
  (r'^save/$', bookmark_save_page),
)   
