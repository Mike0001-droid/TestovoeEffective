from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from django.urls import path, include
from api.views import (
    post_orders, orders,home, post_items, 
    edit_order, delete_order
)
from account.views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),

    path('api/', include_docs_urls(title='API docs')),
    path('users/', include('account.urls', namespace='user')),
    path('users/token/create/', MyTokenObtainPairView.as_view(), name='token_auth'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('api.urls', namespace='orders')),

    path('post_orders/', post_orders, name='post_orders'),
    path('orders/', orders, name='orders'),
    path('edit_order/<int:pk>/', edit_order, name='edit_order'),
    path('delete_order/<int:pk>/', delete_order, name='delete_order'),
    path('post_items/', post_items, name='post_items'),
]