from django.contrib import admin
from .models import Product, Order

admin.site.site_header="KenInventory Dashboard"
# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
