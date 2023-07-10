from rest_framework import serializers
from django.db.models import QuerySet
from .models import Contacts


class ContactSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        if isinstance(instance, QuerySet):
            return super().to_representation(instance.all())
        return super().to_representation(instance)

    class Meta:
        model = Contacts
        fields = ['id', 'first_name', 'last_name', 'email', 'country_code', 'mobile',
                  'event_notification', 'event_types', 'status']
