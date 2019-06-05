from django.shortcuts import render

from .models import *


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

    value_partitions = chunks(values, round(len(values) / num_columns))

    context = {
        "languages": languages,
        "values": values,
        "num_columns": num_columns,
        "value_partitions": value_partitions,
    }
    return render(request, "langvalues/index.html", context)
