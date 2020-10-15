from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register('student', views.StudentProfileViewSet, basename='students')



app_name = 'core'

urlpatterns = [
    # path('', views.HomeView, name='home'),
    path('', include(router.urls)),
]