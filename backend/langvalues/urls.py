from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = format_suffix_patterns([
    path('', views.index),
    path('api/', include([
        path('values/', views.ValueList.as_view()),
        path('values/<int:pk>/', views.ValueDetail.as_view()),
        path('langs/', views.LanguageList.as_view()),
        path('langs/<int:pk>/', views.LanguageDetail.as_view()),
        path('valuelinks/', views.ValueLinkList.as_view()),
        path('valuelinks/<int:pk>/', views.ValueLinkDetail.as_view()),
    ])),
])
