
from django.shortcuts import render
from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Client, Appointment
from .serializers import ClientSerializer, AppointmentSerializer
from django.contrib.auth import get_user_model


User = get_user_model()

@api_view(['GET'])
@permission_classes([AllowAny])
def get_clients(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def add_client(request):
    if request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        clients = Client.objects.filter(user=request.user.id)
        serializer = ClientSerializer(clients, many=True)
    
@api_view(['PUT'])
@permission_classes([AllowAny])
def edit_client(request, pk):
    client = Client.objects.get(id = pk)
    client.first_name = request.data['first_name']
    client.last_name = request.data['last_name']
    client.username = request.data['username']
    client.password = request.data['password']
    client.email = request.data['email']
    client.dob = request.data['dob']
    client.birth_zip = request.data['birth_zip']
    client.birth_time = request.data['birth_time']
    client.save()
    serializer = ClientSerializer(client)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_client(request, pk):
    client = Client.objects.get(id = pk)
    client.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_appointments(request):
    appointments = Appointment.objects.all()
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def add_appointments(request):
    if request.method == 'GET':
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_appointment(request, pk):
    appointment = Appointment.objects.get(id = pk)
    appointment.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([AllowAny])
def edit_appointment(request, pk):
    appointment = Appointment.objects.get(id = pk)
    appointment.date = request.data['date']
    appointment.time = request.data['time']
    appointment.notes = request.data['notes']
    appointment.save()
    serializer = AppointmentSerializer(appointment)
    return Response(serializer.data)
    