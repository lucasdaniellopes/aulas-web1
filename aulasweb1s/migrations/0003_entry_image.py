# Generated by Django 5.1.2 on 2024-10-31 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aulasweb1s', '0002_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='entries/'),
        ),
    ]
