from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    user_type = models.CharField(max_length=20, choices=[('student', 'Student'), ('admin', 'Admin'), ('vendor', 'Vendor')])

    groups = models.ManyToManyField(
        Group,
        related_name='mainapp_user_groups',  # Add this line
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='mainapp_user_permissions',  # Add this line
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )


    def __str__(self):
        return self.username


class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    service_type = models.CharField(max_length=255)  # e.g., "Food" or "Dry Cleaning"

class Menu(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    nutritional_info = models.TextField(null=True, blank=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    pickup_time = models.DateTimeField()

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

class DryCleaningService(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    garment_type = models.CharField(max_length=255)  # e.g., "Jeans", "Hoodies", "Towels"
    price_per_item = models.DecimalField(max_digits=6, decimal_places=2)

class PickupSchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dry_cleaning_service = models.ForeignKey(DryCleaningService, on_delete=models.CASCADE)
    dropoff_date = models.DateTimeField()
    pickup_date = models.DateTimeField()
