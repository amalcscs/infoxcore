# Generated by Django 3.2.8 on 2022-01-28 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0004_auto_20220125_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='webqr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('qrcode', models.ImageField(blank=True, upload_to='qr_codes')),
            ],
        ),
    ]
