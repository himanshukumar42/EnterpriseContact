# Generated by Django 4.2.3 on 2023-07-06 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contacts_country_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='country_code',
            field=models.CharField(choices=[('+1', 'United States (+1)'), ('+44', 'United Kingdom (+44)'), ('+10', 'Pakistan (+10)'), ('+91', 'India (+91)')], default='+91', max_length=5),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='event_notification',
            field=models.CharField(blank=True, choices=[('all_app_users', 'All Organizational App Users'), ('groups', 'Select Notification Groups')], default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='event_types',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]