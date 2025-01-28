from django.contrib import admin
#from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from api.views import (post_orders, orders,
    home, post_items, edit_order, delete_order,)
from django.urls import path, include

router = routers.DefaultRouter()

urlpatterns = [
    path('', home, name='home'),
    path('post_orders/', post_orders, name='post_orders'),
    path('post_items/', post_items, name='post_items'),
    path('orders/', orders, name='orders'),
    path('docs/', include(router.urls)),
    path('edit_order/<int:pk>/', edit_order, name='edit_order'),
    path('delete_order/<int:pk>/', delete_order, name='delete_order'),

    #path('api/', include_docs_urls(title='API docs')),
    path('admin/', admin.site.urls),
]