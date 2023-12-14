from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def CreateView(request):
    return render(request,'task/index.html')
