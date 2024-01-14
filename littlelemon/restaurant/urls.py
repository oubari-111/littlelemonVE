from django.urls import path, include
from . import views
from .views import MenuItem, bookingview

#app_name = 'restaurant'
#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
urlpatterns = [

    path('menu/', MenuItem.as_view()),
    path('booking/', bookingview.as_view()),
    

    ####### week 1 excesise: setting up the static routes ############
    path('', views.index, name='index'),
    ##############################################



    ##### week 2 exercise: setting up the Menu API
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()), 
    #############################################


    #path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   

]