from rest_framework import serializers

from .models import Dataproduct, Project, Mom2Object, Mom2Objectstatus, LofarBeamMeasurement, LofarDataproduct

# http://localhost:8000/mom3api/dataproducts
class DataproductSerializer_version1(serializers.ModelSerializer):

    class Meta:
        model = Dataproduct
        fields = '__all__'

class DataproductSerializer(serializers.HyperlinkedModelSerializer):
    mom2objectid = serializers.HyperlinkedRelatedField(
        many=False,
        queryset=Mom2Object.objects.all(),
        view_name='mom2object-detail-view',
        lookup_field='pk',
        required=True
    )

    class Meta:
        model = Dataproduct
        fields = ('id','name','indexid','timestamp','type','released','exported','fileformat','archived','pipelined',
                  'topology','status','placeholder','status_code','message','mom2objectid')

class LofarDataproductSerializer(serializers.ModelSerializer):
    class Meta:
        model = LofarDataproduct
        fields = '__all__'

# http://localhost:8000/mom3api/projects
class ProjectSerializer_version1(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    mom2objectid = serializers.HyperlinkedRelatedField(
        many=False,
        queryset=Mom2Object.objects.all(),
        view_name='mom2object-detail-view',
        lookup_field='pk',
        required=True
    )
    class Meta:
        model = Project
        fields = ('id','mom2objectid','releasedate','allowtriggers','priority')

# http://localhost:8000/mom3api/mom2objects
class Mom2ObjectSerializer_version1(serializers.ModelSerializer):

    class Meta:
        model = Mom2Object
        fields = '__all__'


# http://localhost:8000/mom3api/mom2objects
class Mom2ObjectSerializer(serializers.HyperlinkedModelSerializer):
    parentid = serializers.HyperlinkedRelatedField(
        many=False,
        queryset=Mom2Object.objects.all(),
        view_name='mom2object-detail-view',
        lookup_field='pk',
        required=True
    )
    ownerprojectid = serializers.HyperlinkedRelatedField(
        many=False,
        queryset=Mom2Object.objects.all(),
        view_name='mom2object-detail-view',
        lookup_field='pk',
        required=True
    )
    currentstatusid = serializers.HyperlinkedRelatedField(
        many=False,
        queryset=Mom2Objectstatus.objects.all(),
        view_name='mom2objectstatus-detail-view',
        lookup_field='pk',
        required=True
    )

    class Meta:
        model = Mom2Object
        fields = ('id','parentid','indexid','mom2id','mom2objecttype','name','description','ownerprojectid',
                  'currentstatusid','topology','predecessor','topology_parent','group_id','datasize')



class Mom2ObjectStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mom2Objectstatus
        fields = '__all__'


class LofarBeamMeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = LofarBeamMeasurement
        fields = '__all__'