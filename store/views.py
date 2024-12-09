from django.shortcuts import render,  redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        forms = SignupForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('login')
    else:
        forms = SignupForm()

    context = {
        "forms": forms
    }
    return render(request, 'registration/signup.html', context)    

def log_out(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def fruits(request):
    fruits = Product.objects.all()
    context = {
        "fruits": fruits
    }
    return render(request, 'fruits.html', context)


@login_required
def contact_me(request):
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        email = request.POST['email']
        message = request.POST['message']
        print(f"{name}, {number}, {email}, {message}")
    return render(request, 'contact_me.html')


@login_required
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer    
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitems.all()
    else:
        items = []
        order = {"cart_total_item": 0, "cart_total_price":0}
      
    context = {
        "items": items,
        "order":order

    

    }
    return render(request, 'cart.html', context)


