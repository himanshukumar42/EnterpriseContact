from django.urls import path
from .views import health_check, ContactsList, ContactsCreate, ContactsUpdate, ContactsDelete
from .views import ContactsGetAPIView, ContactsPostAPIView, ContactsUpdateAPIView, create_contact, edit_contact

urlpatterns = [
    path('health', health_check, name='health_check'),
    path('', ContactsList.as_view(), name='index'),
    path('contacts-create/', ContactsCreate.as_view(), name='contact-create'),
    path('contacts-update/<int:pk>', ContactsUpdate.as_view(), name='contact-update'),
    path('contacts-delete/<int:pk>', ContactsDelete.as_view(), name='contact-delete'),
    path('contacts/', ContactsGetAPIView.as_view(), name='contacts'),
    path('create-contact/', create_contact, name='add-contact'),
    path('edit-contact/<int:pk>', edit_contact, name='edit-contact'),
    path('create-contacts/', ContactsPostAPIView.as_view(), name='create-contacts'),
    path('update-contacts/', ContactsUpdateAPIView.as_view(), name='update-contacts')
]