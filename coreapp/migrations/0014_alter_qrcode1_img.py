# Generated by Django 4.0.1 on 2022-01-29 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0013_alter_qrcode1_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode1',
            name='img',
            field=models.ImageField(default='', max_length=10000, upload_to='img/%y'),
        ),
    ]
