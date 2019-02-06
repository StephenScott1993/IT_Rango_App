from django.apps import AppConfig


from rango import views

class RangoConfig(AppConfig):
    name = 'rango'

# from django.conf.urls import url
# from rango import views
# urlpatterns = [
# url(r'^$', views.index, name='index'),
# ]



# from django.conf.urls import patterns, url
# from rango import views
#
# urlpatterns = patterns('',
#     url(r'^$', views.index, name='index'))
