from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from first.models import SubCategory, Product, FirstCart, Cart
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.views.generic.edit import CreateView
from django.contrib import messages


# Create your views here.
def index(request):
    categories = SubCategory.objects.all()
    products = Product.objects.order_by('-id')[:3]

    cart_size = 0
    if request.user.is_authenticated:
        cart_size = FirstCart.get_cart_size(request.user)

    context = {
        'categories': categories,
        'products': products,
        'cart_size': cart_size,
    }

    return render(request, 'index.html', context)


def like_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    # Check if the user has already liked the product
    if request.user in product.likes.all():
        # Unlike the product
        product.likes.remove(request.user)
        liked = False
    else:
        # Like the product
        product.likes.add(request.user)
        liked = True

    # Return the number of likes and whether the user has liked the product
    return JsonResponse({'likes': product.likes.count(), 'liked': liked})


def about(request):
    return render(request, 'about.html')


def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})


def contact(request):
    return render(request, 'contact.html')


def shop_single(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    related_products = Product.objects.filter(category=product.category).exclude(pk=product_id).order_by('-id')[:3]
    return render(request, 'shop-single.html', {'product': product, 'related_products': related_products})


@login_required(login_url='/login')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    # Check if the user has a cart
    user_cart, created = FirstCart.objects.get_or_create(user=request.user, product=product)

    # If the cart already exists, increment the quantity
    if not created:
        user_cart.quantity += 1
        user_cart.save()

    messages.success(request, f'{product.title} added to your cart!')

    return JsonResponse({'message': f'{product.title} added to your cart!'})


@login_required(login_url='/login')
def viewcart(request):
    user_cart_items = FirstCart.objects.filter(user=request.user)
    return render(request, 'viewcart.html', {'user_cart_items': user_cart_items})


def remove_from_cart(request):
    if request.method == 'POST':
        cart_item_id = request.POST.get('cart_item_id')
        cart_item = get_object_or_404(FirstCart, id=cart_item_id, user=request.user)
        cart_item.delete()
        messages.success(request, f'{cart_item.product.title} removed from your cart.')
    return redirect('first:viewcart')


def pay(request):
    user_cart_items = FirstCart.objects.filter(user=request.user)
    total_amount = sum(cart_item.product.price * cart_item.quantity for cart_item in user_cart_items)

    context = {
        'total_amount': total_amount,
    }

    return render(request, 'pay.html', context)


def confirm_payment(request):
    if request.method == 'POST':
        # Perform payment processing logic here
        # You might want to create an order, handle payment, etc.
        # For simplicity, we'll just clear the user's cart in this example
        FirstCart.objects.filter(user=request.user).delete()

        FirstCart.objects.filter(user=request.user).delete()
        messages.success(request, 'Payment successful. Your order has been placed.')
        messages.info(request, 'Your cart has been cleared.')
    return redirect('first:viewcart')


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('/')
        else:
            messages.error(request, 'Invalid login credentials.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


# @login_required(login_url='/login')
def user_logout(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('/')


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('/')
        else:
            messages.error(request, 'Invalid registration details. Please try again.')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})
