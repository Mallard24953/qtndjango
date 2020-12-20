from rest_framework import fields
from main.models import Paper, ContactForm
from rest_framework.serializers import ModelSerializer


class PaperSerializer(ModelSerializer):
    class Meta:
        model = Paper
        fields = ['name', 'cost']


class ContactFormSerializer(ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ['name']
