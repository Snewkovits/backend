from django.shortcuts import render

from .serializer import ItemSerializer
from .models import Item, ItemType

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getAllItems(request):
    items = Item.objects.all()
    ser = ItemSerializer(items, many = True)
    return Response(ser.data)

