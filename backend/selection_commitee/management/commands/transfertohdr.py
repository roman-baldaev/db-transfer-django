from django.core.management.base import BaseCommand
from selection_commitee.models import Application, Abiturient


class Command(BaseCommand):
    help = 'Transfer abiturient from selection commitee to hr department'

    def add_arguments(self, parser):
        parser.add_argument(
            '--id', dest='id', required=True,
            help='id of abiturient for transfer',
        )

    def handle(self, *args, **options):
        id = options['id']
        abiturient = Abiturient.objects.get(pk=id)
        application = Application.objects.filter(abiturient=abiturient).first()
        application.transfer_to_hrd()

