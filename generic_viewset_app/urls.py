from django.urls import path,include
from generic_viewset_app.views import *
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'course',CourseViewSet,basename='COURSE')




urlpatterns = [
    path ('generic-blog-list/',BlogListAPI.as_view()),
    path ('generic-blog-get/<str:pk>/',BlogGetAPI.as_view()),
    path ('all/<str:pk>/',BlogIndividual.as_view()),
    path('',include(router.urls))
]