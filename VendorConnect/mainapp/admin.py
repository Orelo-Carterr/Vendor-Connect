from django.contrib import admin

# Register your models here.
from .models import User, Vendor, Menu, Order, Review, DryCleaningService, PickupSchedule

admin.site.register(User)
admin.site.register(Vendor)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(DryCleaningService)
admin.site.register(PickupSchedule)