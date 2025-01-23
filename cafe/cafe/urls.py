from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from api.views import OrderViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet, basename='orders')
urlpatterns = [
    path('docs/', include(router.urls)),
    path('api/', include_docs_urls(title='API docs')),
    path('admin/', admin.site.urls),
]