from rest_framework import generics, permissions

from wish.serializers import WishDetailSerializer, WishListSerializer
from wish.models import Wish
from wish.permissions import IsOwnOrReadOnly


class WishCreateView(generics.CreateAPIView):
    serializer_class = WishDetailSerializer


class WishListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = WishListSerializer
    queryset = Wish.objects.all()


class WishDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WishDetailSerializer
    queryset = Wish.objects.all()
    permission_classes = (IsOwnOrReadOnly, )
