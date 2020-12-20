from main.models import Paper, ContactForm
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PaperSerializer, ContactFormSerializer
from main.calculators import calc
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# from .forms import ContactForm


# Create your views here.

def index(request):
    return render(request, "main/index.html")


def contacts(request):
    return render(request, 'main/contacts.html')


class PaperView(ModelViewSet):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer


@api_view(['GET', 'POST'])
def snippet_list(request):

    if request.method == 'POST':
        return Response(request.data, status=status.HTTP_201_CREATED)

