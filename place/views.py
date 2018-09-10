from django.shortcuts import render
from place.models import Place, UserExperience
from place.serializers import PlaceSerializer, UserExperienceSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response



class PlaceList(generics.ListCreateAPIView):
	queryset = Place.objects.all()
	serializer_class = PlaceSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)
	filter_backends = (DjangoFilterBackend, filters.SearchFilter)
	search_fields = ('name',)
	pagination_class = PageNumberPagination

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def get_or_update_place(request,id):
	try:
		place = Place.objects.get(id=id)
	except Place.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = PlaceSerializer(place)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = PlaceSerializer(place, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status.HTTP_404_BAD_REQUEST)
		
	elif request.method == 'DELETE':
		place.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	

class UserExperienceView(generics.ListCreateAPIView):
	queryset = UserExperience.objects.all()
	serializer_class = UserExperienceSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)
	filter_fields = ('User','Place')
	pagination_class = PageNumberPagination	