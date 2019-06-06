from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

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



def get_values(request, id):
    lang = get_object_or_404(Language, pk=id)
    links = lang.valuelink_set.all()
    return JsonResponse({
        'values': [
            {
                "id": link.value.pk,
                "slug": link.value.slug,
                "name": link.value.name,
                "factor": link.factor,
            }
            for link in links
        ],
    })
