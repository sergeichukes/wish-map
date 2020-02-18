from rest_framework import serializers

from wish.models import Wish


class WishDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Wish
        fields = "__all__"


class WishListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wish
        fields = ("id", "name", "price", "user")
