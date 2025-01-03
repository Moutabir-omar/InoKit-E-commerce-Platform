from django.shortcuts import render, redirect
from django.contrib import messages
from shop.models import Product
from .forms import UserRegistrationForm
from django.templatetags.static import static

def home(request):
    products = Product.objects.all()
    return render(request, "shop/home.html", {"products": products})

def about(request):
    omar_image = static('images/omar-profile.jpg')
    return render(request, "core/about.html", {"omar_image": omar_image})

def contact(request):
    return render(request, "core/contact.html")

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now login.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
