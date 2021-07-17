from django.urls import path

from .views import ReviewList, ReviewCreate, ReviewUpdate, ReviewDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page= 'login'), name='logout'),
    path('', ReviewList.as_view(), name='list'),
    path('review-create/', ReviewCreate.as_view(), name='review-create'),
    path('review-update/<int:pk>/', ReviewUpdate.as_view(), name='review-update'),
    path('review-delete/<int:pk>/', ReviewDelete.as_view(), name='review-delete'),
    path('register/', RegisterPage.as_view(), name='register'),
]