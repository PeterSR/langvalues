from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.index),
    path('api/', include([
        path('values/<int:id>', views.get_values, name="get_values"),
    ])),
]
