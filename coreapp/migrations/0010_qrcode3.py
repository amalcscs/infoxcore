# Generated by Django 4.0.1 on 2022-01-29 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0009_alter_qrcode2_qrid'),
    ]

    operations = [
        migrations.CreateModel(
            name='qrcode3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img12', models.ImageField(upload_to='img/%y')),
            ],
        ),
    ]
