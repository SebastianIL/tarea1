from django.urls import path
from . import views
urlpatterns= [
    path('',views.index,name='index'),
    path('proceso',views.procesamiento,name='proceso'),
    path('suma',views.suma,name='suma'),
    path('resta',views.suma,name='resta'),
    path('bienvenida',views.bienvenida,name='bienvenida'),
    path('multiplicacion',views.multiplicacion,name='multipliacion'),
    path('division',views.division,name='division'),

]