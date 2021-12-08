from django.shortcuts import render
from .models import Pizza

# Create your views here.

def index(request):
    '''The Home Page for Pizzeria.'''
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('name')

    context = {'pizzas':pizzas}

    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all() # foreign key is accessed using '_set'
    
    context = {'pizza':pizza, 'toppings':toppings}

    return render(request, 'pizzas/pizza.html', context)
