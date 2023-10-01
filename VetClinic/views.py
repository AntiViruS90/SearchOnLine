from django.shortcuts import render
from .models import *
from  django.views import generic


def index(request):
    animal = VetClinic.objects.all().count()
    doctor = Doctor.objects.all().count()
    context = {'animal': animal, 'doctor': doctor}
    return render(request, 'index.html', context)


class AnimalList(generic.ListView):
    model = Patient