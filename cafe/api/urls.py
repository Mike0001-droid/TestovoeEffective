from rest_framework import routers
from .views import OrderViewSet


router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet, basename='orders')

app_name = 'api'
urlpatterns = router.urls 
