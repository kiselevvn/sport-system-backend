from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "sandbox command"

    def handle(self, *args, **options):
        pass
