from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'eventregistration.views.home', name='home'),
    url(r'^register/$', 'registration.views.register_form', name='register_form'), 
    url(r'^register/barcode/$', 'registration.views.register_barcode', name='register_barcode'),
    url(r'^register/attend/$', 'registration.views.register', name='register'),
    url(r'^register/withdraw/$', 'registration.views.withdraw', name='withdraw'), 
    url(r'^register/search/$', 'registration.views.ajax_user_search', name='search'),

    url(r'^attended/search/$', 'registration.views.search_attend', name='search_attend'),
    url(r'^attended/$', 'registration.views.attended_form', name='attend_form'),
    url(r'^event/$', 'registration.views.event_form', name='event_form'),
    
#    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT } ),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    

    url(r'^login/$', 'auth.views.login_user', name='login'),
    url(r'^logout/$', 'auth.views.logout_user', name='logout'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT } ),
    )

urlpatterns += staticfiles_urlpatterns()

