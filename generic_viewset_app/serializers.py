from rest_framework import serializers
from apiclass_app.models import *
from generic_viewset_app.models import *



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'




class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = '__all__'








class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategoryModel
        fields = '__all__'        



class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model =  SubjectModel
        fields = '__all__'                