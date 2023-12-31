from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Contacts
from .forms import ContactsForm
from rest_framework.views import APIView
from .serializers import ContactSerializer
from django.shortcuts import redirect
from rest_framework.response import Response
from django.template.loader import render_to_string
from django.shortcuts import render
from rest_framework import status
from django.http import QueryDict


@api_view(('GET',))
def health_check(request): # noqa
    return HttpResponse("<h1>Health Ok</h1>")


@api_view(('GET',))
def create_contact(request):
    return render(request, "create.html")


@api_view(('GET',))
def edit_contact(request, pk):
    contact = Contacts.objects.get(pk=pk)
    return render(request, 'edit.html', context={"contact": contact})


class ContactsList(ListView):
    model = Contacts
    context_object_name = 'contacts'
    template_name = 'index.html'


class ContactsCreate(CreateView):
    model = Contacts
    form_class = ContactsForm
    success_url = reverse_lazy('index')


class ContactsUpdate(UpdateView):
    model = Contacts
    fields = '__all__'
    success_url = reverse_lazy('index')


class ContactsDelete(DeleteView):
    model = Contacts
    fields = '__all__'
    success_url = reverse_lazy('index')


class ContactsGetAPIView(APIView):
    def get(self, request):
        contacts = Contacts.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        rendered_html = render_to_string('index.html', {'contacts': serializer.data})
        response = HttpResponse(content_type='text/html')
        response.write(rendered_html)
        return response


class ContactsPostAPIView(APIView):
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
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ContactsUpdateAPIView(APIView):
    def put(self, request, pk):
        instance = self.get_object(pk)
        serializer = ContactSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('index')
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        instance = self.get_object(pk)
        serializer = ContactSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return redirect('index')
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_object(self, pk):
        try:
            return Contacts.objects.get(pk=pk)
        except Contacts.DoesNotExist:
            raise status.HTTP_500_INTERNAL_SERVER_ERROR
