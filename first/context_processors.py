# first/context_processors.py

from .models import FirstCart

def cart_items_count(request):
    if request.user.is_authenticated:
        user_cart_items_count = FirstCart.objects.filter(user=request.user).count()
    else:
        user_cart_items_count = 0

    return {'cart_items_count': user_cart_items_count}
