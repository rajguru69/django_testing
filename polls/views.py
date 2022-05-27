from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.

def blankpage(request):
    return HttpResponse("This is a blank Page (Means idhar kuch nai hai)")

def home(request):
    context = {}
    if request.method == 'POST':
        name =  request.POST.get('name')
        context['name'] = name
    return render(request,'blogs/home.html', context)

def about(request):
    return HttpResponse("this is about Page")

def contact_us(request):
    return HttpResponse("this is Contact Page")

def links(request):
    return HttpResponse("<h1>All Researches of Ramesh singh Rajpurohit \
    </h1><a href = https://www.javatpoint.com/django-crud-application#:~:text=Django%20CRUD%20(Create%20Read%20Update,\
    %24%20django%2Dadmin%20startproject%20crudexample>\
     All Researches</a>")
