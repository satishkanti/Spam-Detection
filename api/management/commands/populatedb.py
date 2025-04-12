import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import Contact

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        # Create users
        for i in range(10):
            user = User.objects.create_user(
                username=f'user{i}',
                phone_number=f'123456789{i}',
                email=f'user{i}@example.com',
                password='password'
            )

            # Create contacts for each user
            for j in range(10):
                Contact.objects.create(
                    user=user,
                    name=f'Contact{j}',
                    phone_number=f'987654321{j}',
                    is_spam=random.choice([True, False])
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
