from django.shortcuts import render


def home_new(request):
    return render(request, 'home_new.html')
