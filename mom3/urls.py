from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

# app imports
from . import views

urlpatterns = [
    # --- REST API ---
    path('dataproducts/', views.DataProductListView.as_view(), name='dataproduct-list-view'),
    path('dataproducts/<int:pk>/', views.DataProductDetailView.as_view(), name='dataproduct-detail-view'),
    path('lofardataproducts/', views.LofarDataProductListView.as_view(), name='lofar-dataproduct-list-view'),
    path('lofardataproducts/<int:pk>/', views.LofarDataProductDetailView.as_view(), name='lofar-dataproduct-detail-view'),
    path('projects/', views.ProjectListView.as_view(), name='project-list-view'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail-view'),
    path('mom2objects/', views.Mom2ObjectListView.as_view(), name='mom2object-list-view'),
    path('mom2objects/<int:pk>/', views.Mom2ObjectDetailView.as_view(), name='mom2object-detail-view'),
    path('mom2objectstatus/<int:pk>/', views.Mom2ObjectStatusDetailView.as_view(),
        name='mom2objectstatus-detail-view'),
    path('lofarbeams', views.LofarBeamsListView.as_view(), name='lofarbeams-list-view'),

    # --- function endpoints ---
    path('getsip/<int:mom2dpid>', views.getsip, name='get-sip'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
