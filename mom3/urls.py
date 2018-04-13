from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

# app imports
from . import views

urlpatterns = [
    url(r'^mom3api/projects$', views.ProjectListView.as_view(), name='project-list-view'),
    url(r'^mom3api/projects/(?P<pk>[0-9]+)/$', views.ProjectDetailView.as_view(), name='project-detail-view'),
    url(r'^mom3api/mom2objects$', views.Mom2ObjectListView.as_view(), name='mom2object-list-view'),
    url(r'^mom3api/mom2objects/(?P<pk>[0-9]+)/$', views.Mom2ObjectDetailView.as_view(), name='mom2object-detail-view'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
