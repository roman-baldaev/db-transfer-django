from django.db import models
import uuid
# Create your models here.


class Faculty(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    out_id = models.UUIDField(primary_key=False, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=256)


class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    out_id = models.UUIDField(primary_key=False, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=256)


class Region(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    out_id = models.UUIDField(primary_key=False, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=256)


class Area(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    out_id = models.UUIDField(primary_key=False, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=256)


class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    out_id = models.UUIDField(primary_key=False, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=256)


class Special(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    out_id = models.UUIDField(primary_key=False, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=256)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)


class Abiturient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=256)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Application(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    abiturient = models.ForeignKey(Abiturient, on_delete=models.CASCADE)
    special = models.ForeignKey(Special, on_delete=models.CASCADE)
    enlisted = models.BooleanField(default=False)
