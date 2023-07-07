from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Contacts
from rest_framework.views import APIView
from .serializers import ContactSerializer
from django.shortcuts import redirect
from rest_framework.response import Response
from django.template.loader import render_to_string
from django.shortcuts import render
from rest_framework import status
from django.http import QueryDict
from django.db.models import Q


@api_view(('GET',))
def health_check(request): # noqa
    return HttpResponse("<h1>Health Ok</h1>")


class ContactsDelete(DeleteView):
    model = Contacts
    fields = '__all__'
    success_url = reverse_lazy('index')


class ContactsSearchAPIVIew(APIView):
    def get(self, request):
        if "search" in request.query_params.keys():
            contacts = Contacts.objects.filter(
                Q(first_name__icontains=request.query_params['search']) |
                Q(last_name__icontains=request.query_params['search']) |
                Q(email__icontains=request.query_params['search']) |
                Q(mobile__icontains=request.query_params['search']) |
                Q(event_types__icontains=request.query_params['search']) |
                Q(status__icontains=request.query_params['search'])
                )
            if "status" in request.query_params.keys():
                contacts = contacts.filter(status=request.query_params['status'])
        elif "search" not in request.query_params.keys() and "status" in request.query_params.keys():
            contacts = Contacts.objects.filter(status=request.query_params['status'])
        else:
            contacts = Contacts.objects.all()

        serializer = ContactSerializer(contacts, many=True)
        rendered_html = render_to_string('index.html', {'contacts': serializer.data})
        response = HttpResponse(content_type='text/html')
        response.write(rendered_html)
        return response


class ContactsGetAPIView(APIView):
    def get(self, request):
        contacts = Contacts.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        rendered_html = render_to_string('index.html', {'contacts': serializer.data})
        response = HttpResponse(content_type='text/html')
        response.write(rendered_html)
        return response


class ContactsPostAPIView(APIView):
    def get(self, request):
        return render(request, "create.html")

    def post(self, request):
        data = request.data
        event_types = ','.join(data.getlist('event_types'))
        new_data = QueryDict(mutable=True)
        new_data.update(data)
        new_data['event_types'] = event_types
        serializer = ContactSerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return redirect('index')
        return render(request, 'create.html')


class ContactsUpdateAPIView(APIView):
    def get(self, request, pk):
        contact = Contacts.objects.get(pk=pk)
        return render(request, 'edit.html', context={"contact": contact})

    def post(self, request, pk):
        instance = self.get_object(pk)
        data = request.data
        event_types = ','.join(data.getlist('event_types'))
        new_data = QueryDict(mutable=True)
        new_data.update(data)
        new_data['event_types'] = event_types
        serializer = ContactSerializer(instance, data=new_data)
        if serializer.is_valid():
            serializer.save()
            return redirect('index')
        return render(request, 'edit.html')

    def patch(self, request, pk):
        instance = self.get_object(pk)
        serializer = ContactSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return redirect('index')
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            contact = self.get_object(pk)
            contact.delete()
            return redirect('index')
        except Contacts.DoesNotExist:
            raise status.HTTP_500_INTERNAL_SERVER_ERROR

    def get_object(self, pk):
        try:
            return Contacts.objects.get(pk=pk)
        except Contacts.DoesNotExist:
            raise status.HTTP_500_INTERNAL_SERVER_ERROR
