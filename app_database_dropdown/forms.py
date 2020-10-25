from django.forms import ModelForm
from .models import *


class CarForm(ModelForm):
    class Meta:
        model = Car
        exclude = [
            'type',
            'user_created',
            'date_created',
        ]
