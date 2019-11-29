from django.core.management import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):

    def handle(self, *args, **options):
        user_model = get_user_model()
        if not user_model.objects.filter(email="admin@admin.com").exists():
            user_model.objects.create_superuser(username="admin", email="admin@admin.com", password="admin123")
