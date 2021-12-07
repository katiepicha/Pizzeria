# the path function, which is needed when mapping URLs to views
from django.urls import path

# the dot tells Python to import the views.py module from the same directory as the current urls.py module
from . import views
import pizzas

# the variable app_name helps Django distinguish this urls.py file from files of the same name in other apps within the project
app_name = 'pizzas'

# the variable urlpatterns in this module is a list of individual pages that can be requested from the pizzas app
urlpatterns = [
    path('', views.index, name = 'index'),
]

