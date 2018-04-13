from django.shortcuts import render
from rest_framework import generics
from django_filters import rest_framework as filters

from .models import Project, Mom2Object, Dataproduct
from .serializers import ProjectSerializer, Mom2ObjectSerializer, DataproductSerializer

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

class DataProductDetailView(generics.ListCreateAPIView):
    queryset = Dataproduct.objects.all()
    serializer_class = DataproductSerializer

class ProjectListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class Mom2ObjectFilter(filters.FilterSet):
    # altapi/ingests?PID=123

    class Meta:
        model = Mom2Object

        fields = {
            'mom2id': ['exact', 'icontains'],
            'group_id': ['exact', 'icontains'],
            'mom2objecttype': ['exact', 'icontains']
        }

class Mom2ObjectListView(generics.ListCreateAPIView):
    queryset = Mom2Object.objects.all()
    serializer_class = Mom2ObjectSerializer
    filter_class = Mom2ObjectFilter

class Mom2ObjectDetailView(generics.ListCreateAPIView):
    queryset = Mom2Object.objects.all()
    serializer_class = Mom2ObjectSerializer

