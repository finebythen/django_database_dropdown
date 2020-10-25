from django.contrib import messages
from django.shortcuts import render, redirect

from .models import *
from .forms import *


def main(request):
    # --> Database-Query
    car_type_db = CarType.objects.all()

    car_type_list = []
    for item in car_type_db:
        car_type_list.append(item.name)

    form = CarForm()

    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user_created = request.user
            form.instance.type = request.POST.get('car_type')
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Eintrag wurde gespeichert!')
            return redirect("Main")
        else:
            messages.add_message(request, messages.WARNING, 'Eintrag konnte nicht erstellt werden!')

    context = {'formset': form, 'car_type_list': car_type_list}
    return render(request, 'app_database_dropdown/main.html', context)
