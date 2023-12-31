from django.urls import path
from apiv2 import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('restaurants/', views.RestaurantList.as_view()),
    path('restaurants/<int:pk>/', views.RestaurantDetail.as_view()),
    path('restaurants/<int:pk>/reviews/', views.ReviewList.as_view()),
    path('restaurants/<int:pk>/reviews/<int:id>/', views.ReviewDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)
