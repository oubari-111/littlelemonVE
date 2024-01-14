from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import MenuSerializer
from django.shortcuts import render
from .models import Booking, Menu
from .serializers import BookingSerializer
################################################################################



def index(request):
    return render(request, 'index.html', {})



## Week 2: Excercise: Set up the menu API ################
class MenuItemsView(generics.ListCreateAPIView):
  permission_classes = [IsAuthenticated]
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
################################################################################
    
class MenuItem(APIView):
   def get(self,request):
      items = Menu.objects.all()
      serializer = MenuSerializer(items, many=True)
      return Response(serializer.data)
   
   def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      



## week 2: exercise: set up the table booking API ################
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
################################################################################
    


class bookingview(APIView):
   def get(self,request):
      items = Booking.objects.all()
      serializer = BookingSerializer(items, many=True)
      return Response(serializer.data)
   

@api_view()

@permission_classes([IsAuthenticated])

def securedview(request):
   return Response({"message":"needs authentication"})




