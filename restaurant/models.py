from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Restaurant(models.Model):
    title = models.CharField(max_length=80)
    address = models.CharField(max_length=80)

    objects = models.Manager

    def __str__(self):
        return self.title


class Menu(models.Model):
    """Menu model. The day field consists of 7 days to choose from.
    Foreign key restaurant id indicates which restaurant it belongs to"""
    MONDAY = 'Mon'
    TUESDAY = 'Tue'
    WEDNESDAY = 'Wed'
    THURSDAY = 'Thu'
    FRIDAY = 'Fri'
    SATURDAY = 'Sat'
    SUNDAY = 'Sun'
    DAYS = [
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    ]
    day = models.CharField(max_length=15, choices=DAYS)
    restaurant = models.ForeignKey('Restaurant', null=True, on_delete=models.PROTECT)

    objects = models.Manager

    def __str__(self):
        return f"{self.restaurant.title}, {self.day}"

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'


class Dishes(models.Model):
    """The dish model. Each dish has a name, price and a foreign key of the menu id to which it belongs"""
    dish = models.CharField(max_length=80)
    price = models.IntegerField()
    menu = models.ForeignKey('Menu', null=True, on_delete=models.PROTECT)

    objects = models.Manager

    def __str__(self):
        return f"{self.menu.restaurant}, {self.dish}"

    class Meta:
        verbose_name = 'Dishes'
        verbose_name_plural = 'Dishes'


class Employee(models.Model):
    """Employee model. As a foreign key there is a base class User"""
    name = models.CharField(max_length=80)
    job = models.CharField(max_length=80)
    menu = models.ForeignKey('Menu', null=True, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = models.Manager

    def __str__(self):
        return self.name

