from rest_framework import serializers
from .models import Contacts


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        fields = ['id', 'first_name', 'last_name', 'email', 'country_code', 'mobile',
                  'event_notification', 'event_types', 'status']
