"""django_restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from restaurant.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include("rest_framework.urls")),
    path('api/v1/restaurant/', RestaurantAPIList.as_view()),

    path('api/v1/menu/', MenuAPIList.as_view()),
    # path('api/v1/menu/<int:pk>/', MenuAPIRetrieve.as_view()),
    path('api/v1/menu/<str:day>/', MenuDayAPIList.as_view()),  # days  in the format (mon, tue, wed, etc.)

    path('api/v1/dishes/', DishesAPIList.as_view()),
    # path('api/v1/dishes/<int:pk>/', DishesAPIRetrieve.as_view()),

    path('api/v1/employee/', EmployeeAPIList.as_view()),
    path('api/v1/employee/menu/<int:pk>/', EmployeeMenuAPIRetrieve.as_view()),

    path('api/v1/result/', EmployeeResultAPIList.as_view()),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
