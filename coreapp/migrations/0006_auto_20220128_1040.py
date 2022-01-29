# Generated by Django 3.2.8 on 2022-01-28 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0005_webqr'),
    ]

    operations = [
        migrations.CreateModel(
            name='QrCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('image', models.ImageField(blank=True, upload_to='qrcode')),
            ],
        ),
        migrations.DeleteModel(
            name='webqr',
        ),
    ]
