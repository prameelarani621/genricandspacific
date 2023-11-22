from django.shortcuts import render

# Create your views here.
def bablu(request):
    return render(request,'bablu.html')

def hansi(request):
    return render(request,'hansi.html')