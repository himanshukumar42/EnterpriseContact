from rest_framework.response import Response
from .models import Contacts
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from rest_framework import viewsets
from .serializers import ContactSerializer
from rest_framework import status
from django.core import serializers
from django.db.models import Q


class ContactsSearchAPIVIew(APIView):
    def get(self, request):
        if "search" in request.query_params.keys():
            contacts = Contacts.objects.filter(
                Q(first_name__icontains=request.query_params['search']) |
                Q(last_name__icontains=request.query_params['search']) |
                Q(email__icontains=request.query_params['search']) |
                Q(mobile__icontains=request.query_params['search']) |
                Q(event_types__icontains=request.query_params['search']) |
                Q(status__icontains=request.query_params['search']) |
                Q(event_notification__icontains=request.query_params['search'])
            )
            if "status" in request.query_params.keys():
                contacts = contacts.filter(status=request.query_params['status'])
        elif "search" not in request.query_params.keys() and "status" in request.query_params.keys():
            contacts = Contacts.objects.filter(status=request.query_params['status'])
        else:
            contacts = Contacts.objects.all()

        serializer = ContactSerializer(contacts, many=True)
        return Response(data=serializer.data, content_type='application/json')


class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer


class ContactsPostAPIView(APIView):
    def get(self, request):
        contacts = Contacts.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(data=serializer.data, content_type='application/json', status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        event_types = ','.join(data.get('event_types'))
        data['event_types'] = event_types
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, content_type='application/json', status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, content_type='application/json', status=status.HTTP_400_BAD_REQUEST)


class ContactsAPIView(APIView):
    def get(self, request, pk):
        try:
            instance = Contacts.objects.get(pk=pk)
        except Contacts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance_dict = model_to_dict(instance)
        serializer = ContactSerializer(data=instance_dict)
        if serializer.is_valid():
            return Response(data=serializer.data, content_type='application/json', status=status.HTTP_200_OK)
        return Response(data=serializer.errors, content_type='application/json', status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        data = request.data
        event_types = ','.join(data.get('event_types'))
        data['event_types'] = event_types
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, content_type='application/json', status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, content_type='application/json', status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            instance = Contacts.objects.get(pk=pk)
        except Contacts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer = ContactSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, content_type='application/json', status=status.HTTP_200_OK)
        return Response(data=serializer.errors, content_type='application/json', status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            instance = Contacts.objects.get(pk=pk)
        except Contacts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer = ContactSerializer(instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, content_type='application/json', status=status.HTTP_200_OK)
        return Response(data=serializer.data, content_type='application/json', status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            instance = Contacts.objects.get(pk=pk)
        except Contacts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
