from rest_framework import serializers
from .models import Value, Language, ValueLink

class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = ['id', 'name', 'slug', ]

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name', 'slug', 'values', ]

class ValueLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValueLink
        fields = ['id', 'language', 'value', 'factor', ]
