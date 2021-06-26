from rest_framework import routers

from django.urls import path, include
from . import views
from django.views.decorators.csrf import csrf_exempt

from rest_framework import routers
router = routers.DefaultRouter()


router.register('users',  views.AuthViewSet, basename='cutareadel')
#...

urlpatterns = [
    path('users/', views.UserCreate.as_view(), name='account-create'),
    path('users/login', views.LoginAPIView.as_view(), name='account-create'),
    path('', include(router.urls)),
   
]
