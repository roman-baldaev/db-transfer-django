from django.core.management.base import BaseCommand
import random
import json
from selection_commitee.models import Faculty, Country, Region, Area, City, Special, Abiturient, Application


def save_list(model, list):
    for item in list:
        new_model = model(name=item)
        new_model.save()


class Command(BaseCommand):
    help = 'Filling test data to sc_db'

    def handle(self, *args, **options):
        with open("data/seed_data.json") as f:
            test_data = json.load(f)
        country = test_data['country']
        print(country)
        region = test_data['region']
        area = test_data['area']
        city = test_data['city']
        faculty = test_data['faculty']
        abiturients = test_data['abiturients']
        save_list(Country, country)
        save_list(Region, region)
        save_list(Area, area)
        save_list(City, city)
        for faculty, special in faculty.items():
            new_faculty = Faculty(name=faculty)
            new_faculty.save()
            for spec in special:
                new_special = Special(name=spec, faculty=new_faculty)
                new_special.save()
        for abiturient in abiturients:
            _country = Country.objects.filter(name=random.choice(country)).first()
            _id_for_place = random.choice(range(len(region)))
            _region = Region.objects.filter(name=region[_id_for_place]).first()
            _area = Area.objects.filter(name=area[_id_for_place]).first()
            _city = City.objects.filter(name=city[_id_for_place]).first()

            new_abiturient = Abiturient(name=abiturient, country=_country, region=_region, area=_area, city=_city)
            new_abiturient.save()
            new_application = Application(abiturient=new_abiturient, special=Special.objects.order_by("?").first(),
                                          enlisted=random.choice([True, False]))
            new_application.save()
