from django.shortcuts import render
from django.http import HttpResponse
from .models import Hero

def form_view(request):
    return render(request, 'form.html')

def contact_view(request):
    if request.method == "POST":
        Hero.objects.create(
            hero_name=request.POST.get('hero_name'),
            age=request.POST.get('age'),
            movies=request.POST.get('movies'),
            dob=request.POST.get('dob'),
            no_of_movies=request.POST.get('no_of_movies')
        )
    return render(request, 'contact.html')

def about_view(request):
    return render(request, 'about.html')

# Create your views here.
