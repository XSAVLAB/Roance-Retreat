# Generated by Django 5.2.1 on 2025-05-14 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surprisekaroapp', '0005_booking_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whatsapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='ourstory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='story/'),
        ),
    ]
