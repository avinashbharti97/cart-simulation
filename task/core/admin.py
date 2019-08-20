from django.contrib import admin
from .models import Product,Cart

# Register your models here.
class ShopAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product)
admin.site.register(Cart)