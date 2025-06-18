from rest_framework import serializers
from .models import Service, TeamMember, Project, Contact, VoiceWork, Order, PaymentTransaction

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'icon', 'price', 'created_at', 'updated_at']

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

class VoiceWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceWork
        fields = ['id', 'title', 'artist', 'audio_file', 'created_at', 'updated_at'] 

class OrderSerializer(serializers.ModelSerializer):
    service_title = serializers.CharField(source='service.title', read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'order_id', 'service', 'service_title', 'customer_name', 'customer_email', 
                 'customer_phone', 'amount', 'currency', 'payment_status', 'payfast_payment_id', 
                 'created_at', 'updated_at']
        read_only_fields = ['order_id', 'payment_status', 'payfast_payment_id']

class PaymentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransaction
        fields = ['id', 'order', 'payfast_payment_id', 'transaction_status', 'amount_paid', 
                 'payment_date', 'payfast_data'] 