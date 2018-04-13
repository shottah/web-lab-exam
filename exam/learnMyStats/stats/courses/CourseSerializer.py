from .Course import Course
from rest_framework import serializers

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = (
            'code', 
            'name',
            'credits'
        )
        