from django.conf.urls import url

from spares_info import views


urlpatterns = [
    url(r'shops/?$', views.shops, name='shops'),
    url(r'shops/(?P<pk>[0-9]+)/?$', views.shops, name='shops'),
    url(r'catalog/?$', views.catalog, name='catalog'),
    url(r'catalog/(?P<pk>[0-9]+)/?$', views.catalog, name='catalog'),
    url(r'catalog_upload/?$', views.catalog_upload, name='catalog_upload'),
    url(r'utils/?$', views.utils, name='utils'),
    url(r'(?P<page_name>.*)/?$', views.page, name='page'),
    url(r'/?$', views.page, name='index'),
]
