from rest_framework.decorators import api_view
from .models import MenuItem
#from .serializers import MenuItemSerializer
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

# Create your views here. 
#class MenuItemsView(generics.ListCreateAPIView):
 #   queryset = MenuItem.objects.all()
  #  serializer_class = MenuItemSerializer

#class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
#    queryset = MenuItem.objects.all()
#    serializer_class = MenuItemSerializer

