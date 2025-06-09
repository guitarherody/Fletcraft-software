from django.core.management.base import BaseCommand
from core.models import Service, TeamMember, Project


class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Populating database with sample data...')

        # Clear existing data
        Service.objects.all().delete()
        TeamMember.objects.all().delete()
        Project.objects.all().delete()

        # Create Services
        services = [
            {
                'title': 'Custom Software Development',
                'description': 'Tailored solutions built with cutting-edge technology to solve your unique business challenges and drive innovation.',
                'icon': 'fas fa-code'
            },
            {
                'title': 'Web Applications',
                'description': 'Powerful, scalable, and responsive web applications that deliver exceptional user experiences across all devices.',
                'icon': 'fas fa-globe'
            },
            {
                'title': 'Mobile Development',
                'description': 'Native and cross-platform mobile apps that engage users and drive business growth in the mobile-first world.',
                'icon': 'fas fa-mobile-alt'
            },
            {
                'title': 'AI & Machine Learning',
                'description': 'Intelligent solutions that leverage the latest in artificial intelligence and machine learning to automate processes.',
                'icon': 'fas fa-robot'
            },
            {
                'title': 'Cloud Solutions',
                'description': 'Scalable cloud infrastructure and services that optimize performance, reduce costs, and ensure reliability.',
                'icon': 'fas fa-cloud'
            },
            {
                'title': 'Cybersecurity',
                'description': 'Comprehensive security solutions to protect your digital assets and maintain data integrity at all times.',
                'icon': 'fas fa-shield-alt'
            }
        ]

        for service_data in services:
            Service.objects.create(**service_data)

        # Create Team Members
        team_members = [
            {
                'name': 'Dylan Fletcher',
                'position': 'CEO & Lead Developer',
                'bio': 'Visionary leader with over 10 years of experience in software development and business strategy. Passionate about creating innovative solutions that drive real business value.',
                'image': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400'
            },
            {
                'name': 'Sarah Chen',
                'position': 'Full-Stack Developer',
                'bio': 'Expert full-stack developer specializing in modern web technologies. Loves building scalable applications with clean, maintainable code.',
                'image': 'https://images.unsplash.com/photo-1494790108755-2616b332c1fe?w=400'
            },
            {
                'name': 'Marcus Rodriguez',
                'position': 'AI/ML Engineer',
                'bio': 'Machine learning specialist with a PhD in Computer Science. Focuses on developing intelligent systems that solve complex business problems.',
                'image': 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400'
            },
            {
                'name': 'Emily Watson',
                'position': 'UI/UX Designer',
                'bio': 'Creative designer with a passion for user-centered design. Creates beautiful, intuitive interfaces that users love to interact with.',
                'image': 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=400'
            },
            {
                'name': 'Alex Kim',
                'position': 'DevOps Engineer',
                'bio': 'Infrastructure expert who ensures our applications run smoothly. Specializes in cloud platforms, CI/CD, and security best practices.',
                'image': 'https://images.unsplash.com/photo-1507591064344-4c6ce005b128?w=400'
            }
        ]

        for member_data in team_members:
            TeamMember.objects.create(**member_data)

        # Create Projects
        projects = [
            {
                'title': 'E-Commerce Platform Revolution',
                'description': 'A comprehensive e-commerce platform with AI-powered recommendations, real-time inventory management, and advanced analytics. Built for scale with microservices architecture.',
                'image': 'https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=600',
                'url': 'https://demo-ecommerce.fletcraft.com'
            },
            {
                'title': 'Healthcare Management System',
                'description': 'Secure patient management system with real-time monitoring, appointment scheduling, and comprehensive reporting for healthcare providers.',
                'image': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1f?w=600',
                'url': 'https://demo-healthcare.fletcraft.com'
            },
            {
                'title': 'FinTech Trading Platform',
                'description': 'High-frequency trading platform with real-time market data, advanced charting, and AI-powered trading signals for professional traders.',
                'image': 'https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=600',
                'url': 'https://demo-fintech.fletcraft.com'
            },
            {
                'title': 'Smart City IoT Dashboard',
                'description': 'Real-time monitoring and control system for smart city infrastructure, including traffic management, energy optimization, and environmental monitoring.',
                'image': 'https://images.unsplash.com/photo-1480714378408-67cf0d13bc1f?w=600',
                'url': 'https://demo-smartcity.fletcraft.com'
            },
            {
                'title': 'Learning Management System',
                'description': 'Modern LMS with interactive content delivery, progress tracking, and AI-powered personalized learning paths for educational institutions.',
                'image': 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=600',
                'url': 'https://demo-lms.fletcraft.com'
            },
            {
                'title': 'Real Estate CRM',
                'description': 'Comprehensive CRM solution for real estate agencies with property management, client tracking, and automated marketing workflows.',
                'image': 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=600',
                'url': 'https://demo-realestate.fletcraft.com'
            }
        ]

        for project_data in projects:
            Project.objects.create(**project_data)

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created:\n'
                f'- {len(services)} services\n'
                f'- {len(team_members)} team members\n'
                f'- {len(projects)} projects'
            )
        ) 