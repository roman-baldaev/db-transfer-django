from django.contrib import admin
from .models import Faculty, Country, Region, Area, City, Special, Abiturient, Application
# Register your models here.
sc_admin = admin.AdminSite('sc_admin')
sc_admin.register(Faculty)
sc_admin.register(Country)
sc_admin.register(Region)
sc_admin.register(Area)
sc_admin.register(City)
sc_admin.register(Special)
sc_admin.register(Abiturient)
sc_admin.register(Application)
