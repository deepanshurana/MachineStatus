from rest_framework import routers 
from django.urls import path, include
from .views import mAView

router = routers.DefaultRouter()
router.register('', mAView, base_name='apiView')

urlpatterns = [
    path('', include(router.urls)),
]