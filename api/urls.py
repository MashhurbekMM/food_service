from django.urls import path, include

from rest_framework.routers import DefaultRouter

from food_service import views
from .yasg import urlpatterns as yasg_urlpatterns


router = DefaultRouter()

router.register('foods', views.FoodViewSet)
router.register('categories', views.CategoriesViewSet)
router.register('foodMakeups', views.FoodMakeupViewSet)
router.register('foodSizes', views.FoodSizeViewSet)
router.register('foodWeights', views.FoodWeightViewSet)
router.register('orderFood', views.OrderFoodViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('api.auth.urls')),
]

urlpatterns += yasg_urlpatterns