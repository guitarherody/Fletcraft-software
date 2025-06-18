from django.db import models
import uuid

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="Price in ZAR")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField(blank=True)
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']

class VoiceWork(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='voice_works/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.artist}"

class Order(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
    ]
    
    order_id = models.CharField(max_length=50, unique=True, default=uuid.uuid4)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='ZAR')
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    payfast_payment_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.order_id} - {self.customer_name}"

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = str(uuid.uuid4())
        super().save(*args, **kwargs)

class PaymentTransaction(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payfast_payment_id = models.CharField(max_length=100)
    transaction_status = models.CharField(max_length=50)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payfast_data = models.JSONField(default=dict)

    def __str__(self):
        return f"Payment {self.payfast_payment_id} for Order {self.order.order_id}"
