from rest_framework import serializers
from authentication.serializers import UserSerializer

from .models import Meal, Menu, Customer, Admin, Order

class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admin
        fields = ['first_name', 'last_name']

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name']

class AddMealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meal
        fields = ['id', 'name', 'description', 'price', 'image']

class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meal
        fields = ['id', 'name', 'description', 'price', 'image', 'created_at']

class CreateMenuSerializer(serializers.ModelSerializer):

    # menu_meals = MealSerializer()

    class Meta:
        model = Menu
        fields = ['id', 'menu_meals', 'date']

    def create(self, validated_data):
        admin = Admin.objects.get(user_id=self.context['admin_id'])
        menu = Menu.objects.create(created_by=admin, **validated_data)
        return menu

class MenuSerializer(serializers.ModelSerializer):

    menu_meals = MealSerializer()
    created_by = AdminSerializer()

    class Meta:
        model = Menu
        fields = ['id', 'menu_meals', 'date', 'created_by']

class AddOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'customer', 'menu', 'chosen_meal']

class OrderSerializer(serializers.ModelSerializer):

    customer = CustomerSerializer()
    menu = MenuSerializer()
    chosen_meal = MealSerializer()

    class Meta:
        model = Order
        fields = ['id', 'customer', 'menu', 'chosen_meal', 'created_at']