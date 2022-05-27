from django.urls import path
from . import views
urlpatterns = [

    path('', views.blankpage),
    path('home/', views.home,name='polls-home'),
    path('about/', views.about,name='about'),
    path('contact_us/', views.contact_us,name='contact'),
    path('links/', views.links),

]
