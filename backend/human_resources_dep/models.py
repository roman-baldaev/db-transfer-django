from django.db import models

# Create your models here.
from django.db import models
import uuid
# Create your models here.


class Faculty(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=False)
    name = models.CharField(max_length=256)

    def __str__(self):
        return '{}, id: {}'.format(self.name, self.id)


class Country(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=False)
    name = models.CharField(max_length=256)

    def __str__(self):
        return '{}, id: {}'.format(self.name, self.id)


class Region(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=False)
    name = models.CharField(max_length=256)

    def __str__(self):
        return '{}, id: {}'.format(self.name, self.id)


class Area(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=False)
    name = models.CharField(max_length=256)

    def __str__(self):
        return '{}, id: {}'.format(self.name, self.id)


class City(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=False)
    name = models.CharField(max_length=256)

    def __str__(self):
        return '{}, id: {}'.format(self.name, self.id)


class Special(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=False)
    name = models.CharField(max_length=256)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}, id: {}'.format(self.name, self.faculty.name, self.id)


class Abiturient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({}, {})".format(self.name, self.country.name, self.city.name)


class Application(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    abiturient = models.ForeignKey(Abiturient, on_delete=models.CASCADE)
    special = models.ForeignKey(Special, on_delete=models.CASCADE)
    enlisted = models.BooleanField(default=True)

    def __str__(self):
        return "{} - {} ({}), {}".format(self.abiturient.name, self.special.name, self.special.faculty.name, self.enlisted)
