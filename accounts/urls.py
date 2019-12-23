from django.contrib import admin
from . import views
from django.urls import path
from .views import MyProfileView, ProfileView, FollowProfile

urlpatterns = [
  path('', MyProfileView.as_view(), name='my-profile'),
  path('<slug:slug>', ProfileView.as_view(), name="view-profile"),
  path('<slug:slug>/follow', FollowProfile, name="follow-profile")



]