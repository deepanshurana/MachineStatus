from rest_framework import viewsets
from machineApp.models import MOD 
from machineApp.api.serializers import mASerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

class mAView(viewsets.ModelViewSet):
    queryset = MOD.objects.all()
    serializer_class = mASerializer
