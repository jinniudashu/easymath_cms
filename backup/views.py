from django.shortcuts import render

from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Backup


class BackupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backup
        fields = '__all__'

@api_view(['GET'])
def data_backup(request):
    data_backups = [Backup.objects.last()]
    serializer = BackupSerializer(data_backups, many=True)
    return Response(serializer.data)
