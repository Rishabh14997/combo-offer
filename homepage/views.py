from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'homepage/home.html')

def contact(request):
    return render(request,'homepage/basic.html',{'content': ['If you would like to contact me, please email me','rishabh23jain@gmail.com']})