from django.urls import path
from wish.views import WishCreateView, WishListView, WishDetailView

app_name = 'wish'

urlpatterns = [
    path('wish/create/', WishCreateView.as_view()),
    path('wish/', WishListView.as_view()),
    path('wish/detail/<int:pk>/', WishDetailView.as_view()),
]
