from django.shortcuts import render
from .serializers import ItemSerializer

from rest_framework import mixins, generics, status
from .models import Item
from rest_framework.response import Response

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

class ItemDetail(mixins.RetrieveModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):

    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ItemList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
     
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        items = Item.objects.filter(user=request.user).order_by('id')
        
        page_size = self.request.query_params.get('page_size', 10)
        page_number = self.request.query_params.get('page_number', 1)

        paginator = Paginator(items, page_size)

        try:
           items = paginator.page(page_number)
        except PageNotAnInteger:
           items = paginator.page(1)
        except EmptyPage:
           items = paginator.page(paginator.num_pages)
        
        count = paginator.count

        previous = None if not items.has_previous(
        ) else items.previous_page_number()

        next = None if not items.has_next(
        ) else items.next_page_number()

        serializer = ItemSerializer(items, many=True)
        
        self.data = {
            'count': count,
            'previous': previous,
            'next': next,
            'items': serializer.data
        }
        return Response(self.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
 
