from django.contrib import admin
from .models import ShopKeeper, Clients, History,Feedback

# Register your models here.
admin.site.register(ShopKeeper)
admin.site.register(Clients)
admin.site.register(History)
admin.site.register(Feedback)