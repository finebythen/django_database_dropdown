from django.db import models


class CarType(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    user_created = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Car(models.Model):
    license_plate = models.CharField(max_length=20, null=False, blank=False)
    type = models.CharField(max_length=50, null=False, blank=False)
    user_created = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.license_plate
