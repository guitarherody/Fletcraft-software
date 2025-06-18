#!/usr/bin/env python3
import os
import sys
import django

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Service
from decimal import Decimal

def add_prices_to_services():
    """Add test prices to existing services"""
    
    # Test prices between R200 and R500
    test_prices = [
        Decimal('250.00'),  # R250
        Decimal('350.00'),  # R350
        Decimal('450.00'),  # R450
        Decimal('300.00'),  # R300
        Decimal('400.00'),  # R400
        Decimal('200.00'),  # R200
    ]
    
    services = Service.objects.all()
    
    if not services.exists():
        print("No services found. Creating some test services...")
        # Create some test services if none exist
        test_services = [
            {
                'title': 'Web Development',
                'description': 'Custom web applications built with modern technologies',
                'icon': 'fas fa-code',
                'price': Decimal('450.00')
            },
            {
                'title': 'Mobile App Development',
                'description': 'Native and cross-platform mobile applications',
                'icon': 'fas fa-mobile-alt',
                'price': Decimal('350.00')
            },
            {
                'title': 'AI & Machine Learning',
                'description': 'Intelligent solutions powered by artificial intelligence',
                'icon': 'fas fa-robot',
                'price': Decimal('500.00')
            },
            {
                'title': 'Cloud Solutions',
                'description': 'Scalable cloud infrastructure and deployment',
                'icon': 'fas fa-cloud',
                'price': Decimal('300.00')
            },
            {
                'title': 'Cybersecurity',
                'description': 'Security audits and protection services',
                'icon': 'fas fa-shield-alt',
                'price': Decimal('400.00')
            },
            {
                'title': 'UI/UX Design',
                'description': 'Beautiful and intuitive user interfaces',
                'icon': 'fas fa-palette',
                'price': Decimal('250.00')
            }
        ]
        
        for service_data in test_services:
            Service.objects.create(**service_data)
            print(f"Created service: {service_data['title']} - R{service_data['price']}")
    
    else:
        print(f"Found {services.count()} existing services. Adding prices...")
        
        for i, service in enumerate(services):
            if i < len(test_prices):
                service.price = test_prices[i]
                service.save()
                print(f"Updated {service.title} - R{service.price}")
            else:
                service.price = Decimal('300.00')  # Default price
                service.save()
                print(f"Updated {service.title} - R{service.price} (default)")
    
    print("\n✅ All services now have prices!")
    print("You can now test the payment system on your website.")

if __name__ == '__main__':
    add_prices_to_services() 