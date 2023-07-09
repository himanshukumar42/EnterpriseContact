from django.urls import path
from .views import ContactsDelete
from .views import ContactsSearchAPIVIew, ContactsPostAPIView, ContactsUpdateAPIView

urlpatterns = [
    path('', ContactsSearchAPIVIew.as_view(), name='index'),
    path('contacts-delete/<int:pk>', ContactsDelete.as_view(), name='contact-delete'),
    path('create-contacts/', ContactsPostAPIView.as_view(), name='create-contacts'),
    path('update-contacts/<int:pk>/', ContactsUpdateAPIView.as_view(), name='update-contacts')
]