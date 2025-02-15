from django.urls import path, include

from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewset, basename='hello-viewset')
router.register('profile', views.UserProfileViewset, basename='profile')
router.register('login', views.LoginUserViewset, basename='login')
router.register('profile_feed_item', views.UserProfileFeedViewset, basename='profile_feed_item')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]