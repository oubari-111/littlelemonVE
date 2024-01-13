from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets

from .models import booking, MenuItem
from .serializers import BookingSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated



from .models import MenuItem
from .serializers import MenuItemSerializer
from django.shortcuts import render




def index(request):
    return render(request, 'index.html', {})

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
  permission_classes = [IsAuthenticated]
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class bookingview(APIView):
   def get(self,request):
      items = booking.objects.all()
      serializer = BookingSerializer(items, many=True)
      return Response(serializer.data)



class MenuItem(APIView):
   def post(self, request):
      serializer = MenuItemSerializer(datarequest.data)
      if serializer.is_valid():
         serializer.save()
         return Response({"status": "success", "data": serializer.data})
      
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = booking.objects.all()
    serializer_class = BookingSerializer
    

@api_view()

@permission_classes([IsAuthenticated])

def securedview(request):
   return Response({"message":"needs authentication"})
