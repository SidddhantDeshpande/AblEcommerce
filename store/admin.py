from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.volunteer import Volunteer



class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price' , 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer)
admin.site.register(Volunteer)
admin.site.register(Order)
