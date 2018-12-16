from django.db import models
import uuid
from human_resources_dep.models import (Faculty as HRDFaculty, Country as HRDCountry, Region as HRDRegion,
                                        Area as HRDArea, City as HRDCity, Special as HRDSpecial)
# Create your models here.


class Faculty(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    out_id = models.UUIDField(primary_key=False, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=256)

    def __str__(self):
        return '{}, id: {}, out_id: {}'.format(self.name, self.id, self.out_id)

    def save(self, *args, **kwargs):
        super(Faculty, self).save(*args, **kwargs)
        hrd_fac = HRDFaculty(id=self.out_id, name=self.name)
        hrd_fac.save()


class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    out_id = models.UUIDField(primary_key=False, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=256)

    def __str__(self):
        return '{}, id: {}, out_id: {}'.format(self.name, self.id, self.out_id)

    def save(self, *args, **kwargs):
        super(Country, self).save(*args, **kwargs)
        hrd_country = HRDCountry(id=self.out_id, name=self.name)
        hrd_country.save()


class Region(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    out_id = models.UUIDField(primary_key=False, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=256)

    def __str__(self):
        return '{}, id: {}, out_id: {}'.format(self.name, self.id, self.out_id)

    def save(self, *args, **kwargs):
        super(Region, self).save(*args, **kwargs)
        hrd_region = HRDRegion(id=self.out_id, name=self.name)
        hrd_region.save()


class Area(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    out_id = models.UUIDField(primary_key=False, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=256)

    def __str__(self):
        return '{}, id: {}, out_id: {}'.format(self.name, self.id, self.out_id)

    def save(self, *args, **kwargs):
        super(Area, self).save(*args, **kwargs)
        hrd_area = HRDArea(id=self.out_id, name=self.name)
        hrd_area.save()


class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    out_id = models.UUIDField(primary_key=False, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=256)

    def __str__(self):
        return '{}, id: {}, out_id: {}'.format(self.name, self.id, self.out_id)

    def save(self, *args, **kwargs):
        super(City, self).save(*args, **kwargs)
        hrd_city = HRDCity(id=self.out_id, name=self.name)
        hrd_city.save()


class Special(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    out_id = models.UUIDField(primary_key=False, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=256)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}, id: {}, out_id: {}'.format(self.name, self.faculty.name, self.id, self.out_id)

    def save(self, *args, **kwargs):
        super(Special, self).save(*args, **kwargs)
        hrd_special = HRDSpecial(id=self.out_id, name=self.name, faculty_id=self.faculty.out_id)
        hrd_special.save()


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
