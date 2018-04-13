from rest_framework import serializers

from .models import Dataproduct, Project, Mom2Object

# http://localhost:8000/mom3api/dataproducts
class DataproductSerializer_version1(serializers.ModelSerializer):

    class Meta:
        model = Dataproduct
        fields = '__all__'

class DataproductSerializer(serializers.HyperlinkedModelSerializer):
    mom2objectid = serializers.HyperlinkedRelatedField(
        many=False,
        # read_only=True,
        queryset=Mom2Object.objects.all(),
        view_name='mom2object-detail-view',
        lookup_field='pk',
        required=True
    )

    class Meta:
        model = Dataproduct
        fields = ('id','name','indexid','timestamp','type','released','exported','fileformat','archived','pipelined',
                  'topology','status','placeholder','status_code','message','mom2objectid')

# http://localhost:8000/mom3api/projects
class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

# http://localhost:8000/mom3api/mom2objects
class Mom2ObjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mom2Object
        fields = '__all__'

