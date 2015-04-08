from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'telit_request.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^telit-post-request/$', 'telit_request.views.telit_post_request', name='telit_post_request'),
    url(r'^admin/', include(admin.site.urls)),
)
