from django.db import router
from django.urls import path, include

from profile_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello_viewset',views.HelloViewSet,basename ='hello_viewset')
router.register('profile',views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)
urlpatterns = [
    path('hello_view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('',include(router.urls))
]