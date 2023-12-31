# Generated by Django 4.2.3 on 2023-07-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='country_code',
            field=models.CharField(choices=[('+1', 'United States (+1)'), ('+44', 'United Kingdom (+44)'), ('+91', 'India (+91)')], default='+1', max_length=5),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='event_notification',
            field=models.CharField(blank=True, choices=[('all_app_users', 'All Organization App Users'), ('groups', 'Groups')], default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='event_types',
            field=models.CharField(blank=True, choices=[('sos', 'SOS'), ('all', 'all'), ('timer', 'timer'), ('safe_walk', 'Safe WALK')], default=None, max_length=100, null=True),
        ),
    ]
