from django.shortcuts import render, get_object_or_404
from rest_framework import generics

from .models import *
from .serializers import *


class ValueList(generics.ListCreateAPIView):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer

class ValueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer



class LanguageList(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class LanguageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer



class ValueLinkList(generics.ListCreateAPIView):
    queryset = ValueLink.objects.all()
    serializer_class = ValueLinkSerializer

class ValueLinkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ValueLink.objects.all()
    serializer_class = ValueLinkSerializer
