from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def index(request):
    return render(request,"generator/home.html")
def pas(request):

    words = list('qwertyuiopasdfghjklzxcvbnm')
    passw = ''
    length = int(request.GET.get('length',12))
    if request.GET.get('special'):
        words.extend(list('!@#$%^&*'))
    if request.GET.get('Upper'):
        words.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('numbers'):
        words.extend(list('!@#$%^&*'))


    for i in range (length):
        passw += random.choice(words)


    return render(request,"generator/password.html",{'pass':passw})


def about(request):
    return render(request, 'generator/about.html')
