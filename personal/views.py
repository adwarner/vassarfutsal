from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'personal/home.html') 

def teams(request):
    return render(request,'personal/basic.html',
                  {'content':['Team1: Adam Mitch HVB Tanner','JP STILL SUCKS','T-GIL Is A Cache']})

def results(request):
    return render(request,'personal/results.html',
                  {'stuff':['Results']})

def lifting(request):
    return render(request,'personal/lifting.html')
