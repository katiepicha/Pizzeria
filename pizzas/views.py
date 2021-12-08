from django.shortcuts import render, redirect
from .forms import CommentForm
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

def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = CommentForm()
    else:
        # POST data submitted, process data
        form = CommentForm(data=request.POST)
        # check to see if all required fields have been filled
        if form.is_valid():
            # write the data from the form to the database
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()
            form.save()
            return redirect('pizzas:pizza', pizza_id=pizza_id)

    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizzas/new_comment.html', context)

