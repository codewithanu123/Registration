from django.http import JsonResponse
from .models import UserD
from .serializers import MyAPISerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])

def UserD_list(request):

    #get all the user details
    #serialize them
    #return json

    if request.method == 'GET':
        details = UserD.objects.all()
        serializer = MyAPISerializer(details, many = True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MyAPISerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])

def UserD_detail(request, id):

    try:
        detail = UserD.objects.get(pk=id)

    except UserD.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
            
    if request.method == 'GET':
        serializer = MyAPISerializer(detail)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MyAPISerializer(detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
       UserD.delete()
       return Response(status= status.HTTP_204_NO_CONTENT)



    
