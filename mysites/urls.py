from django.contrib import admin
from django.urls import path,include


from .views import Landing_Page
urlpatterns = [
    path('',Landing_Page.as_view())
]