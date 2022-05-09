from django import views
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index ,name ='i'),
    path("about/", views.about,name="AboutUS"),
    path("contact/", views.contact,name="ContactUS"),
    path("tracker/", views.tracker,name="TrackingStatus"),
    path("search/", views.search,name="Search"),
    path("products/<int:myid>", views.productView,name="prodsearch"),
    path("checkout/",views.checkout,name="checkout")
    

]
