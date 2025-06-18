from django.contrib import admin
from .models import Service, TeamMember, Project, Contact, VoiceWork, Order, PaymentTransaction

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description']
    list_editable = ['price']

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'position']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject']
    list_editable = ['is_read']

@admin.register(VoiceWork)
class VoiceWorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'artist']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'customer_name', 'service', 'amount', 'payment_status', 'created_at']
    list_filter = ['payment_status', 'created_at']
    search_fields = ['order_id', 'customer_name', 'customer_email']
    readonly_fields = ['order_id', 'created_at', 'updated_at']

@admin.register(PaymentTransaction)
class PaymentTransactionAdmin(admin.ModelAdmin):
    list_display = ['payfast_payment_id', 'order', 'transaction_status', 'amount_paid', 'payment_date']
    list_filter = ['transaction_status', 'payment_date']
    search_fields = ['payfast_payment_id', 'order__order_id']
    readonly_fields = ['payment_date']
