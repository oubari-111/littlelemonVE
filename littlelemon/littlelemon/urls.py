"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views
from rest_framework.authtoken.views import obtain_auth_token


# week 2: exercise: set up the table booking API ################
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)
###########################################################

urlpatterns = [

    ########## Week 1: Exercise: Setting up the static routes #########
    path('admin/', admin.site.urls),

    path('restaurant/', include('restaurant.urls')),
    ###########################################################

    ##### week 2 exercise: setting up the Menu API #########
    path('restaurant/menu/',include('restaurant.urls')),
    ###########################################################

    ##### week 2: exercise: set up the table booking API ################
    path('restaurant/booking/', include(router.urls)),
    ###########################################################

    ##### week 3: exercise: add the registration page 
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    ############################################

    ##### week 3: exercose: securing the table booking API
    path('api-token-auth/', obtain_auth_token),
    ############################################



    #path('', include('restaurant.urls')),
    #path('api/', include('restaurant.urls')),
    

]
