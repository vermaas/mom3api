from rest_framework import serializers

from .models import Project, Mom2Object

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