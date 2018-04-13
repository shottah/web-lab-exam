from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'courses', views.CourseViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'create_course$', views.create_course, name='create_course'),
    url(r'^api/', include(router.urls))
]