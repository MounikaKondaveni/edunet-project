import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_restaurant.settings')
django.setup()

from menu.models import FoodItem

for item in FoodItem.objects.all():
    item.price = round(random.uniform(100.0, 500.0), 2)
    item.save()

print("Prices updated successfully to Rupees range!")
