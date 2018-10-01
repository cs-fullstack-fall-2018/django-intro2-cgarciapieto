from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('hello_name/', views.hello_name),
    path('times2/', views.times2),
    path('sumofNumber/', views.sumofNumber),
    path('<int:number1>/times2/', views.times2)
]