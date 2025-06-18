from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.management import call_command
from core.models import Service
from decimal import Decimal
import os

class Command(BaseCommand):
    help = 'Set up admin user, run migrations, and add prices to services for production'

    def handle(self, *args, **options):
        # Run migrations first
        self.stdout.write('🔄 Running migrations...')
        call_command('migrate', verbosity=0)
        self.stdout.write(self.style.SUCCESS('✅ Migrations completed'))

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
            self.stdout.write('ℹ️  Superuser already exists')

        # Create sample services if none exist
        services = Service.objects.all()
        if not services.exists():
            self.stdout.write('🔄 Creating sample services...')
            sample_services = [
                {
                    'title': 'Custom Software Development',
                    'description': 'Tailored software solutions built to meet your specific business needs',
                    'icon': 'fas fa-code',
                    'price': Decimal('450.00')
                },
                {
                    'title': 'Web Applications',
                    'description': 'Modern, responsive web applications with cutting-edge technology',
                    'icon': 'fas fa-globe',
                    'price': Decimal('350.00')
                },
                {
                    'title': 'Mobile Development',
                    'description': 'Native and cross-platform mobile applications for iOS and Android',
                    'icon': 'fas fa-mobile-alt',
                    'price': Decimal('400.00')
                },
                {
                    'title': 'AI & Machine Learning',
                    'description': 'Intelligent solutions powered by artificial intelligence and ML algorithms',
                    'icon': 'fas fa-robot',
                    'price': Decimal('500.00')
                },
                {
                    'title': 'Cloud Solutions',
                    'description': 'Scalable cloud infrastructure and deployment services',
                    'icon': 'fas fa-cloud',
                    'price': Decimal('300.00')
                },
                {
                    'title': 'Cybersecurity',
                    'description': 'Comprehensive security audits and protection services',
                    'icon': 'fas fa-shield-alt',
                    'price': Decimal('250.00')
                }
            ]
            
            for service_data in sample_services:
                Service.objects.create(**service_data)
                self.stdout.write(
                    f'✅ Created service: {service_data["title"]} - R{service_data["price"]}'
                )
        else:
            # Add prices to existing services if they don't have prices
            test_prices = [
                Decimal('250.00'),  # R250
                Decimal('350.00'),  # R350
                Decimal('450.00'),  # R450
                Decimal('300.00'),  # R300
                Decimal('400.00'),  # R400
                Decimal('200.00'),  # R200
            ]
            
            self.stdout.write(f'🔄 Updating {services.count()} existing services...')
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

        self.stdout.write(
            self.style.SUCCESS('\n🎉 Setup complete! You can now:')
        )
        self.stdout.write('1. Access admin at: /admin/')
        self.stdout.write('2. Test payments on your website')
        self.stdout.write('3. Manage services and orders')
        self.stdout.write('4. API endpoints are ready at: /api/services/') 