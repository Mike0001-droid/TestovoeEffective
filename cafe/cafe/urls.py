from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from api.views import post_orders, orders, home
from django.urls import path, include

router = routers.DefaultRouter()

urlpatterns = [
    path('', home),
    path('post_orders/', post_orders),
    path('orders/', orders),
    path('docs/', include(router.urls)),
    path('api/', include_docs_urls(title='API docs')),
    path('admin/', admin.site.urls),
]