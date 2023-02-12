from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.messages import constants as messages
from rest_framework.response import Response
from .models import CsvFiles
from .serializers import CsvFilesSerializer
from rest_framework import status
import os
import pandas as pd


@api_view(('GET', 'PUT', ))
@authentication_classes([])
@permission_classes([])
def upload_csv(request):
    if request.method == 'GET':
        request.data['user'] = request.user.id
        csv = CsvFiles.objects.all()
        serializer = CsvFilesSerializer(csv, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        csv_file = request.FILES.get('file')
        name =  request._full_data['fileName']
        dict = {'name':name, 'csv':csv_file}
        serializer = CsvFilesSerializer(data=dict)
        if serializer.is_valid():
            serializer.save()

            # get current path of file
            path = os.getcwd()
            file_directory = path +'\FileReceiver\\'+name
            print(file_directory)

            # read_csv file 
            read_csv(file_directory)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def read_csv(filename):
    pass




