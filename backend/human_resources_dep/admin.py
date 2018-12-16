from django.contrib import admin
from .models import Faculty, Country, Region, Area, City, Special, Abiturient, Application
# Register your models here.
hrd_admin = admin.AdminSite('hrd_admin')
hrd_admin.register(Faculty)
hrd_admin.register(Country)
hrd_admin.register(Region)
hrd_admin.register(Area)
hrd_admin.register(City)
hrd_admin.register(Special)
hrd_admin.register(Abiturient)
hrd_admin.register(Application)
