from django.contrib import admin
from .models import Product
from .models import CartItem

admin.site.register(CartItem)
admin.site.register(Product)
