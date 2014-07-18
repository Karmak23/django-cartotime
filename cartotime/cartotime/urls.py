from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


from views import TimelineList, CartoTimeView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cartotime.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^timeline/', include("timelinejs.urls")),
    url(r'^cartotime/(?P<pk>\d+)/$', CartoTimeView.as_view(),
        name='cartotimeview'),
    url(r'^$', TimelineList.as_view()),
)
