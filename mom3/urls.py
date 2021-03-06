from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

# app imports
from . import views

urlpatterns = [
    url(r'^mom3api/dataproducts$', views.DataProductListView.as_view(), name='dataproduct-list-view'),
    url(r'^mom3api/dataproducts/(?P<pk>[0-9]+)/$', views.DataProductDetailView.as_view(), name='dataproduct-detail-view'),
    url(r'^mom3api/projects$', views.ProjectListView.as_view(), name='project-list-view'),
    url(r'^mom3api/projects/(?P<pk>[0-9]+)/$', views.ProjectDetailView.as_view(), name='project-detail-view'),
    url(r'^mom3api/mom2objects$', views.Mom2ObjectListView.as_view(), name='mom2object-list-view'),
    url(r'^mom3api/mom2objects/(?P<pk>[0-9]+)/$', views.Mom2ObjectDetailView.as_view(), name='mom2object-detail-view'),
    url(r'^mom3api/mom2objectstatus/(?P<pk>[0-9]+)/$', views.Mom2ObjectStatusDetailView.as_view(),
        name='mom2objectstatus-detail-view'),
    url(r'^mom3api/lofarbeams', views.LofarBeamsListView.as_view(), name='lofarbeams-list-view'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
