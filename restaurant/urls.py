from django.urls import path 
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('menu-items', views.MenuItemsViewSet.as_view({'get': 'list', 'post': 'list'})),
    # path('menu-items/<int:pk>', views.MenuItemsViewSet.as_view({'get': 'retrieve'})),
    path('items', views.MenuView.as_view()),
    path('items/<int:pk>', views.SingleMenuView.as_view()),
    # path('cart/menu-items', views.CartView.as_view()),
    # path('orders', views.OrderView.as_view()),
    # path('orders/<int:pk>', views.SingleOrderView.as_view()),
    # path('category', views.CategoriesView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    # path('groups/manager/users', views.managers),
    # path('groups/delivery-crew/users', views.delivery_crew),
]