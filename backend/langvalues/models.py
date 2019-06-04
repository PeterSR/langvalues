from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Value(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=64)
    values = models.ManyToManyField(Value, through='ValueLink')

    def __str__(self):
        return self.name

class ValueLink(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    value = models.ForeignKey(Value, on_delete=models.CASCADE)
    factor = models.FloatField(
        default=1.0,
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],
    )
