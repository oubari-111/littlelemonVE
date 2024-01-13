from django.urls import path, include
from . import views
from .views import MenuItem, bookingview

app_name = 'restaurant'
#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
urlpatterns = [

    path('menu/', MenuItem.as_view()),
    path('booking/', bookingview.as_view()),
    
    path('', views.index, name='index'),
    #path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()), 
]