from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from first import views


app_name = "first"


urlpatterns = [
    path('', views.index, name="index"),
    path('shop/', views.shop, name="shop"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    # path('contact/', views.shop_single, name="shop-single"),
    path('shop-single/<int:product_id>/', views.shop_single, name='shop-single'),
    path('like/<int:product_id>/', views.like_product, name='like_product'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('viewcart/', views.viewcart, name='viewcart'),
    path('remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
    path('pay/', views.pay, name='pay'),
    path('confirm_payment/', views.confirm_payment, name='confirm_payment'),

                  path('login/', views.user_login, name='login'),
                  path('logout/', views.user_logout, name='logout'),
                  path('register/', views.user_register, name='signup'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
