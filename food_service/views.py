from rest_framework.viewsets import ModelViewSet
from food_service.models import Food, Categories, FoodMakeup, FoodSize, FoodWeight, OrderFood
from food_service.serializers import FoodSerializer, CategoriesSerializer, FoodMakeupSerializer, FoodSizeSerializer, FoodWeightSerializer, OrderFoodSerializer



class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class CategoriesViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class FoodMakeupViewSet(ModelViewSet):
    queryset = FoodMakeup.objects.all()
    serializer_class = FoodMakeupSerializer


class FoodSizeViewSet(ModelViewSet):
    queryset = FoodSize.objects.all()
    serializer_class = FoodSizeSerializer


class FoodWeightViewSet(ModelViewSet):
    queryset = FoodWeight.objects.all()
    serializer_class = FoodWeightSerializer


class OrderFoodViewSet(ModelViewSet):
    queryset = OrderFood.objects.all()
    serializer_class =OrderFoodSerializer