from rest_framework import serializers
from machineApp.models import MOD


class mASerializer(serializers.ModelSerializer):
    class Meta: 
        model = MOD
        fields = '__all__'
    
    