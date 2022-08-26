from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('add/<int:prod_id>/',views.add_cart,name='add_cart'),
    path('',views.cart_detail,name='cart_detail'),
    path('remove/<int:prod_id>/',views.cart_remove,name='cart_remove'),
    path('delete/<int:prod_id>/', views.cart_delete, name='cart_delete'),

]