from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from itertools import chain

from .models import *
from .serializers import *


class RestaurantAPIList(generics.ListCreateAPIView):
    """Class outputs a list of all restaurants.
    Allows you to add new restaurants. Fields (Title, Address)"""
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    # permission_classes = (IsAuthenticated, )


class MenuAPIList(generics.ListCreateAPIView):
    """Class outputs a list of existing menus.
    Allows you to add new menus. Field (Day, Restaurant)"""
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsAuthenticated, )


# class MenuAPIRetrieve(generics.RetrieveAPIView):
#     """ Class displays a specific menu """
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer
#     permission_classes = (IsAuthenticated, )


class MenuDayAPIList(generics.ListAPIView):
    """Class that returns dishes related to one day of the week.
    Takes the day of the week, then pulls out the indexes and combines the dishes related to that index.
    days  in the format (mon, tue, wed, etc.)"""
    serializer_class = DishesSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        day = self.kwargs['day']
        menu_id = Menu.objects.filter(day=day.title())
        result = list(chain(*[Dishes.objects.filter(menu=_.pk) for _ in menu_id]))
        return result


class DishesAPIList(generics.ListCreateAPIView):
    """The class outputs a list of all dishes.
    Allows you to add new dishes. Fields (Dish, Price, Menu)"""
    queryset = Dishes.objects.all()
    serializer_class = DishesSerializer
    permission_classes = (IsAuthenticated, )


# class DishesAPIRetrieve(generics.RetrieveAPIView):
#     """Class displays a specific dish"""
#     queryset = Dishes.objects.all()
#     serializer_class = DishesSerializer
#     permission_classes = (IsAuthenticated, )


class EmployeeAPIList(generics.ListCreateAPIView):
    """Class allows you to create and display a list of employees.
    Fields (Name, Job)"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated,)


class EmployeeMenuAPIRetrieve(generics.RetrieveUpdateAPIView):
    """Class allows you to select the worker menu"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated, )


class EmployeeResultAPIList(generics.ListAPIView):
    """Class return current user menus"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
