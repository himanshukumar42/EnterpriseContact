from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactsSearchAPIVIew, ContactsAPIView, ContactsPostAPIView, ContactsViewSet

router = DefaultRouter()
router.register(r'', ContactsViewSet)

urlpatterns = [
    path('', ContactsSearchAPIVIew.as_view(), name='index'),
    path('contact-view/', include(router.urls)),
    path('contacts/', ContactsPostAPIView.as_view(), name='contacts-create'),
    path('contacts/<int:pk>/', ContactsAPIView.as_view(), name='contacts-update'),
]