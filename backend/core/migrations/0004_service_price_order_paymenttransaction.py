# Generated by Django 5.0.2 on 2025-06-18 09:00

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_voicework'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Price in ZAR', max_digits=10),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default=uuid.uuid4, max_length=50, unique=True)),
                ('customer_name', models.CharField(max_length=200)),
                ('customer_email', models.EmailField(max_length=254)),
                ('customer_phone', models.CharField(blank=True, max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(default='ZAR', max_length=3)),
                ('payment_status', models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid'), ('failed', 'Failed'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('payfast_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.service')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payfast_payment_id', models.CharField(max_length=100)),
                ('transaction_status', models.CharField(max_length=50)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('payfast_data', models.JSONField(default=dict)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.order')),
            ],
        ),
    ]
