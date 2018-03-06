from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Pet

def home(request):
    print(request)
    pets = Pet.objects.all()
    return render(request, 'adoptions/home.html', {'pets': pets})


def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'adoptions/pet_detail.html', {'pet': pet})