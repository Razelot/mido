"""mido URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import os
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.views.generic import RedirectView
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^', include('compendium.urls')),

    ]

urlpatterns += [
        url(r'^static/(?P<path>.*)$', serve, {
            'document_root': settings.STATIC_ROOT,
        }),
        url(r'^favicon\.ico$', RedirectView.as_view(
            # url='/static/compendium/img/favicon.ico', permanent=True
            url=os.path.join(settings.STATIC_ROOT, 'compendium/img/favicon.ico')
        )),
    ]


# #Serve static files from runserver if in dev mode with S3 off.
# if DEBUG and not AWS_STORAGE:
#     urlpatterns += staticfiles_urlpatterns()
