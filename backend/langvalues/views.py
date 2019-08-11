from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics

from .models import *
from .serializers import *


def chunks(l, n):
    """
    Create len(l)/n chunks of size n from list l.
    """
    for i in range(0, len(l), n):
        yield l[i:i+n]

def index(request):

    languages = Language.objects.order_by("name")
    values = Value.objects.order_by("name")

    num_columns = 3
    k = max(round(len(values) / num_columns), 1)

    value_partitions = chunks(values, k)

    context = {
        "languages": languages,
        "values": values,
        "num_columns": num_columns,
        "value_partitions": value_partitions,
    }
    return render(request, "langvalues/index.html", context)



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
