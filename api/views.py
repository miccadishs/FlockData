from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
def breed_list(request):
    list = Breed.objects.all()
    serializer = BreedSerializer(list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def breed_type_list(request):
    print(request.data)
    list = BreedType.objects.all()
    serializer = BreedTypeSerializer(list, many=True)
    return  Response(serializer.data)


@api_view(['GET'])
def owner_list(request):
    print(request.data)
    list = Owner.objects.all()
    serializer = OwnerSerializer(list, many=True)
    return  Response(serializer.data)


@api_view(['GET'])
def country_list(request):
    print(request.data)
    list = Country.objects.all()
    serializer = CountrySerializer(list, many=True)
    return  Response(serializer.data)

#this is working
@api_view(['GET'])
def farm_list(request, uid):
    print(request.data)
    list = Farm.objects.filter(farm_attendant__uid=uid)
    serializer = FarmSerializer(list, many=True)
    return  Response(serializer.data)


@api_view(['GET'])
def flock_list(request):
    print(request.data)
    list = Flock.objects.all()
    serializer = FlockSerializer(list, many=True)
    return  Response(serializer.data)

@api_view(['GET'])
def site_list(request):
    print(request.data)
    list = Site.objects.all()
    serializer = SiteSerializer(list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def house_list(request):
    print(request.data)
    list = House.objects.all()
    serializer = HouseSerializer(list, many=True)
    return  Response(serializer.data)

@api_view(['GET'])
def record_list(request):
    print(request.data)
    list = Record.objects.all()
    serializer = RecordSerializer(list, many=True)
    return  Response(serializer.data)


@api_view(['GET'])
def target_list(request):
    print(request.data)
    list = Target.objects.all()
    serializer = TargetSerializer(list, many=True)
    return  Response(serializer.data)


@api_view(['GET'])
def target_details_list(request):
    print(request.data)
    list = House.objects.all()
    serializer = HouseSerializer(list, many=True)
    return  Response(serializer.data)

@api_view(['GET'])
def vaccination_list(request):
    print(request.data)
    list = Vaccination.objects.all()
    serializer = VaccinationSerializer(list, many=True)
    return  Response(serializer.data)


@api_view(['GET'])
def vaccine_list(request):
    print(request.data)
    list = Vaccine.objects.all()
    serializer = VaccineSerializer(list, many=True)
    return  Response(serializer.data)


@api_view(['POST'])
def record_create(request):
    serializer = RecordSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.data, status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def adjustment_list(request):
    print(request.data)
    list = Adjustment.objects.all()
    serializer = AdjustmentSerializer(list, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def adjustment_create(request):
    serializer = AdjustmentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
