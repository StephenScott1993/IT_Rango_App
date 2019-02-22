"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.conf.urls import url
# from django.contrib import admin
# from django.conf.urls import include
# from django.conf import settings
# from django.conf.urls.static import static
# from rango import views
# from registration.backends.simple.views import RegistrationView
#
#
# class MyRegistrationView(RegistrationView):
#     def get_success_url(self, user):
#         return '/rango/'
#
#
# urlpatterns = [
#     url(r'^$', views.homepage, name='index'),
#     url(r'^rango/', include('rango.urls')),
#     url(r'^admin/', admin.site.urls),
#     url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
#     url(r'^accounts/', include('registration.backends.simple.urls')),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from registration.backends.simple.views import RegistrationView

# Create a new class that redirects the user to the index page,
#if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/rango/'



from rango import views
urlpatterns = [
url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
url(r'^accounts/', include('registration.backends.simple.urls')),
url(r'^$', views.index, name='index'),
url(r'^rango/', include('rango.urls')),
# above maps any URLs starting
# with rango/ to be handled by
# the rango application
url(r'^admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
