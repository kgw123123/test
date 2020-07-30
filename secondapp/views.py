from django.shortcuts import render
from django.http import HttpResponse
from .models import Hospital

def index1(request):
    return HttpResponse('index1')
def main(request):
    return HttpResponse('main!')
def show(request):
    hospital = Hospital.objects.all()
    return render(request, 'show2.html',{'list':hospital})

# Create your views here.
