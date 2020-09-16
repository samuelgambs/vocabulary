from django.db import models

# Create your models here.


class Texts(models.Model):
    primary_text = models.TextField(null=True, blank=True)
    second_text = models.TextField(null=True, blank=True)
    result = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Textos"

