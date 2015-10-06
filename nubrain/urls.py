"""nubrain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from nubrain.settings import BASE_URL, APP_NAME
from django.views.generic import RedirectView
from django.utils.translation import ugettext_lazy

urlpatterns = patterns('',
    (r'^$', RedirectView.as_view(url='%s/admin/' % BASE_URL)),
    url(r'^admin/', include(admin.site.urls)),
)

admin.site.site_title = ugettext_lazy(APP_NAME)
admin.site.site_header = ugettext_lazy('%s Admin' % APP_NAME)
admin.site.index_title = ugettext_lazy('%s Dashboard' % APP_NAME)
admin.autodiscover()
