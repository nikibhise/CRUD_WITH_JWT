from .models import Person
from .serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(http_method_names=['POST',])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def Create_person(request):
    try:
        serializer =  PersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response(data={'detail': 'Error processing request'}, status=status.HTTP_400_BAD_REQUEST)

@api_view()
def show_persons(request):
    try :
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={'detail': 'Error fetching request'}, status=status.HTTP_400_BAD_REQUEST)

@api_view()    
def retrieve_person(request, pk=None):
    try:
        person = get_object_or_404(Person, pk=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={'detail': 'Error fetching request'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['PUT','PATCH'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_person(request, pk=None):
    try:
        person = get_object_or_404(Person,pk=pk)
        if request.method == 'PUT':
            serializer = PersonSerializer(data=request.data, instance=person)
        if request.method =='PATCH':
            serializer = PersonSerializer(data=request.data, instance=person, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={'detail': 'Error fetching request'}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(http_method_names=['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_person(request, pk=None):
    try:
        person = get_object_or_404(Person, pk=pk)
        person.delete()
        return Response(data={'detail':'Person deleted sucessfully'}, status=status.HTTP_200_OK)    

    except Exception as e:
        return Response(data={'detail':'Person deleting person'}, status=status.HTTP_400_BAD_REQUEST)

    
    




