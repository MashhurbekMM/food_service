from django.contrib import admin
from food_service.models import Categories, FoodMakeup, FoodSize, FoodWeight, Food, OrderFood




@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(FoodMakeup)
class FoodMakeupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'categories')
    list_display_links = ('id', 'name', 'categories')
    search_fields = ('id', 'name', 'categories')


@admin.register(FoodSize)
class FoodSizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'food', 'price')
    list_display_links = ('id', 'name', 'food', 'price')
    search_fields = ('id', 'name', 'food', 'price')



@admin.register(FoodWeight)
class FoodWeightAdmin(admin.ModelAdmin):
    list_display = ('id', 'food', 'value')
    list_display_links = ('id', 'food', 'value')
    search_fields = ('id', 'food', 'value')


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'description')


@admin.register(OrderFood)
class OrderFoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'food', 'email', 'phone', 'address', 'comment')
    list_display_links = ('id', 'name', 'food', 'phone', 'address')
    search_fields = ('id', 'name', 'food', 'phone', 'address')