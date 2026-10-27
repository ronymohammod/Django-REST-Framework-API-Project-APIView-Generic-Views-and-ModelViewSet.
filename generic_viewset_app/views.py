# from django.shortcuts import render


from rest_framework import generics
from generic_viewset_app.serializers import *
from generic_viewset_app.models import*
from rest_framework.viewsets import ModelViewSet


class BlogListAPI(generics.ListAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer


class BlogGetAPI(generics.RetrieveAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer


class BlogIndividual(generics.RetrieveUpdateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer





class CourseViewSet(ModelViewSet):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer

