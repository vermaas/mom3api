
from rest_framework import generics, pagination
from django_filters import rest_framework as filters
from django.http import JsonResponse

from .models import Project, Mom2Object, Dataproduct, LofarDataproduct, Mom2Objectstatus, LofarBeamMeasurement
from .serializers import ProjectSerializer, Mom2ObjectSerializer, DataproductSerializer, Mom2ObjectStatusSerializer, \
    LofarBeamMeasurementSerializer, LofarDataproductSerializer

from .services import LofarSIPExportXMLDelegate

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

class DataProductListView(generics.ListAPIView):
    queryset = Dataproduct.objects.all().order_by('id')
    serializer_class = DataproductSerializer
    filterset_class = DataproductFilter

class DataProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dataproduct.objects.all()
    serializer_class = DataproductSerializer

class LofarDataproductFilter(filters.FilterSet):

    class Meta:
        model = LofarDataproduct

        fields = {
            'mom2_dp_id': ['exact', 'icontains'],
            'group_id': ['exact', 'icontains'],
            'archive_id': ['exact', 'icontains'],
            #'dataproductid': ['exact'],
            #'dataproductid__name': ['exact', 'icontains']
        }

class LofarDataProductListView(generics.ListAPIView):
    queryset = LofarDataproduct.objects.all().order_by('id')
    serializer_class = LofarDataproductSerializer
    filterset_class = LofarDataproductFilter

class LofarDataProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LofarDataproduct.objects.all()
    serializer_class = LofarDataproductSerializer

class ProjectFilter(filters.FilterSet):

    class Meta:
        model = Project

        fields = {
            'id': ['exact', 'icontains'],
        }

class ProjectListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_class = ProjectFilter

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

class Mom2ObjectListView(generics.ListAPIView):
    queryset = Mom2Object.objects.all()
    serializer_class = Mom2ObjectSerializer
    filterset_class = Mom2ObjectFilter

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


# ---------- Command endpoint views ----------
def getsip(request, mom2dpid = None):

    if not mom2dpid:
        return JsonResponse({"error": "no mom2dpid given"}, status=400)

    try:
        sip = algorithms.getsip(mom2dpid)
        content = {
            "mom2dpid" : mom2dpid,
            "sip": sip
        }
        return JsonResponse(content)

    except:
        return JsonResponse(
            {"error": "could not generate SIP"}, status=404
        )