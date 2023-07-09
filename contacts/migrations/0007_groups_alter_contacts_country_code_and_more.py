# Generated by Django 4.2.3 on 2023-07-07 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_alter_contacts_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='contacts',
            name='country_code',
            field=models.CharField(choices=[('+91', 'India (+91)'), ('+1', 'United States (+1)'), ('+86', 'China (+86)'), ('+44', 'United Kingdom (+44)'), ('+33', 'France (+33)'), ('+81', 'Japan (+81)'), ('+49', 'Germany (+49)'), ('+7', 'Russia (+7)'), ('+55', 'Brazil (+55)'), ('+61', 'Australia (+61)'), ('+92', 'Pakistan (+92)'), ('+34', 'Spain (+34)'), ('+39', 'Italy (+39)'), ('+52', 'Mexico (+52)'), ('+27', 'South Africa (+27)'), ('+971', 'United Arab Emirates (+971)'), ('+1', 'Canada (+1)'), ('+65', 'Singapore (+65)'), ('+81', 'South Korea (+82)'), ('+358', 'Finland (+358)')], default='+91', max_length=5),
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='groups',
        ),
        migrations.AddField(
            model_name='contacts',
            name='groups',
            field=models.ManyToManyField(to='contacts.groups'),
        ),
    ]
