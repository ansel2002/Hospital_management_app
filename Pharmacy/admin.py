from django.contrib import admin
from . models import Store,Cart,CartItems,Billing
# Register your models here.
admin.site.register(Store)
admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(Billing)
