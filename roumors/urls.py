from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from links.views import LinkListView,UserProfileDetailView,UserProfileEditView
from django.contrib.auth.decorators import login_required as auth

urlpatterns = patterns('',
    # Examples:
    url(r'^$', LinkListView.as_view(),name="home"),
    url(r'^login/$',"django.contrib.auth.views.login",{"template_name":"login.html"},name="login"),
    url(r'^logout/$',"django.contrib.auth.views.logout_then_login",name="logout"),
    url(r'^accounts/',include('registration.backends.simple.urls')),
    url(r'^users/(?P<slug>\w+)/$',UserProfileDetailView.as_view(),name="profile"),
    url(r'edit_profile/$',auth(UserProfileEditView.as_view()),name="edit_profile"),
    # url(r'^roumors/', include('roumors.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
