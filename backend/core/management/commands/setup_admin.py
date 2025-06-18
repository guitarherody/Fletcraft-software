from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Service
from decimal import Decimal
import os

class Command(BaseCommand):
    help = 'Set up admin user and add prices to services for production'

    def handle(self, *args, **options):
        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='originalherody@gmail.com',
                password='Fletcraft2024!'
            )
            self.stdout.write(
                self.style.SUCCESS('✅ Superuser created successfully!')
            )
            self.stdout.write('Username: admin')
            self.stdout.write('Password: Fletcraft2024!')
        else:
            self.stdout.write('Superuser already exists')

        # Add prices to services if they don't have prices
        services = Service.objects.all()
        if services.exists():
            test_prices = [
                Decimal('250.00'),  # R250
                Decimal('350.00'),  # R350
                Decimal('450.00'),  # R450
                Decimal('300.00'),  # R300
                Decimal('400.00'),  # R400
                Decimal('200.00'),  # R200
            ]
            
            for i, service in enumerate(services):
                if not service.price or service.price == 0:
                    price = test_prices[i % len(test_prices)]
                    service.price = price
                    service.save()
                    self.stdout.write(
                        f'✅ Updated {service.title} - R{service.price}'
                    )
                else:
                    self.stdout.write(
                        f'ℹ️  {service.title} already has price: R{service.price}'
                    )
        else:
            self.stdout.write('No services found')

        self.stdout.write(
            self.style.SUCCESS('\n🎉 Setup complete! You can now:')
        )
        self.stdout.write('1. Access admin at: /admin/')
        self.stdout.write('2. Test payments on your website')
        self.stdout.write('3. Manage services and orders') 