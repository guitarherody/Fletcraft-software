from rest_framework import serializers
from .models import Service, TeamMember, Project, Contact

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'icon', 'created_at', 'updated_at']

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['id', 'name', 'position', 'bio', 'image', 'created_at', 'updated_at']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'image', 'url', 'created_at', 'updated_at']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']  # Exclude internal fields 