from django.conf.urls import url

from spares_info import views


urlpatterns = [
    url(r'info/?$', views.info, name='info'),
    url(r'contacts/?$', views.contacts, name='contacts'),
    url(r'shops/(?P<pk>[0-9]+)/?$', views.shops, name='shops'),
    url(r'shops/?$', views.shops, name='shops'),
    url(r'catalog/?$', views.catalog, name='catalog'),
    url(r'catalog_upload/?$', views.catalog_upload, name='catalog_upload'),
    url(r'utils/?$', views.utils, name='utils'),
    url(r'/?$', views.index, name='index'),
]
