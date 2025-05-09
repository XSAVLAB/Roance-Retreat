from django.urls import path
from surprisekaroapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('service/',views.services,name="service"),
    path('inquery/', views.inquery, name= "inquery"),
    path('booking/',views.book_service, name= "booking"),

]