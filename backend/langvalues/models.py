from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from autoslug import AutoSlugField


class Value(models.Model):
    name = models.CharField(max_length=64)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=64)
    slug = AutoSlugField(populate_from='name')
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

    def __str__(self):
        return "{} has value {}".format(self.language, self.value)
