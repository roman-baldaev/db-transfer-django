from django.core.management.base import BaseCommand
from selection_commitee.models import Application


class Command(BaseCommand):
    help = 'Show abiturients with enlisted = True'

    def handle(self, *args, **options):
        enlisted = Application.objects.filter(enlisted=True)
        for application in enlisted:
            print("{} - {} id: {}".format(application.abiturient.name, application.special.name,
                                          application.abiturient.id))
