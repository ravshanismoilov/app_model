from django.shortcuts import render
from django.http import HttpResponse




def get_name(request):
    return HttpResponse('<h1>Laziz Adhamov</h1>')