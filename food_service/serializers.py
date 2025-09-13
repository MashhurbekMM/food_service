from rest_framework.serializers import ModelSerializer
from food_service.models import Food, Categories, FoodMakeup, FoodSize, FoodWeight, OrderFood



class FoodSerializer(ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class FoodMakeupSerializer(ModelSerializer):
    class Meta:
        model = FoodMakeup
        fields = '__all__'



class FoodSizeSerializer(ModelSerializer):
    class Meta:
        model = FoodSize
        fields = '__all__'



class FoodWeightSerializer(ModelSerializer):
    class Meta:
        model = FoodWeight
        fields = '__all__'


class OrderFoodSerializer(ModelSerializer):
    class Meta:
        model = OrderFood
        fields = '__all__'