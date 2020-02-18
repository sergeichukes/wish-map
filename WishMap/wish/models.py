from django.db import models
from django.contrib.auth import get_user_model

WISH_LEVEL_CHOICES = (
    (1, 'Me'),
    (2, 'Friends'),
    (3, 'All'),
)

User = get_user_model()


class Wish(models.Model):
    """
    Класс описывает желание, которое добавляется пользователями

    """
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    # image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField()
    visibility = models.IntegerField(choices=WISH_LEVEL_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
