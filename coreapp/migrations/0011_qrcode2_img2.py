# Generated by Django 4.0.1 on 2022-01-29 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0010_qrcode3'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode2',
            name='img2',
            field=models.ImageField(default='', upload_to='img/%y'),
        ),
    ]