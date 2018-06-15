from django.shortcuts import render
from rest_framework import generics, pagination
from django_filters import rest_framework as filters

from .models import Project, Mom2Object, Dataproduct, Mom2Objectstatus, LofarBeamMeasurement
from .serializers import ProjectSerializer, Mom2ObjectSerializer, DataproductSerializer, Mom2ObjectStatusSerializer, \
    LofarBeamMeasurementSerializer

# Create your views here.
class DataproductFilter(filters.FilterSet):

    class Meta:
        model = Dataproduct

        fields = {
            'id': ['exact', 'icontains'],
            'name': ['exact', 'icontains'],
            'type': ['exact', 'icontains'],
            'mom2objectid__id': ['exact', 'icontains']
        }

class DataProductListView(generics.ListCreateAPIView):
    queryset = Dataproduct.objects.all()
    serializer_class = DataproductSerializer
    filter_class = DataproductFilter

class DataProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dataproduct.objects.all()
    serializer_class = DataproductSerializer

class ProjectListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class Mom2ObjectFilter(filters.FilterSet):
    class Meta:
        model = Mom2Object

        fields = {
            'id': ['exact', 'icontains'],
            'name': ['exact', 'icontains'],
            'mom2id': ['exact', 'icontains'],
            'group_id': ['exact', 'icontains'],
            'mom2objecttype': ['exact', 'icontains']
        }

class Mom2ObjectListView(generics.ListCreateAPIView):
    queryset = Mom2Object.objects.all()
    serializer_class = Mom2ObjectSerializer
    filter_class = Mom2ObjectFilter

class Mom2ObjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mom2Object.objects.all()
    serializer_class = Mom2ObjectSerializer

class Mom2ObjectStatusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mom2Objectstatus.objects.all()
    serializer_class = Mom2ObjectStatusSerializer


class LofarBeamsPagination(pagination.PageNumberPagination):
    page_size = 10000

class LofarBeamsListView(generics.ListCreateAPIView):
    queryset = LofarBeamMeasurement.objects.all()
    serializer_class = LofarBeamMeasurementSerializer
    pagination_class=LofarBeamsPagination