from django.shortcuts import render,redirect


# Create your views here.
def home(request):
    return render(request,'home.html')
def contact(request):
    print(request.POST)
    return render(request,'contact.html')
