from django.db import models

COUNTRY_CHOICES = (
    ('+91', 'India (+91)'),
    ('+1', 'United States (+1)'),
    ('+86', 'China (+86)'),
    ('+44', 'United Kingdom (+44)'),
    ('+33', 'France (+33)'),
    ('+81', 'Japan (+81)'),
    ('+49', 'Germany (+49)'),
    ('+7', 'Russia (+7)'),
    ('+55', 'Brazil (+55)'),
    ('+61', 'Australia (+61)'),
    ('+92', 'Pakistan (+92)'),
    ('+34', 'Spain (+34)'),
    ('+39', 'Italy (+39)'),
    ('+52', 'Mexico (+52)'),
    ('+27', 'South Africa (+27)'),
    ('+971', 'United Arab Emirates (+971)'),
    ('+1', 'Canada (+1)'),
    ('+65', 'Singapore (+65)'),
    ('+81', 'South Korea (+82)'),
    ('+358', 'Finland (+358)')
)

NOTIFY = (
    ('all_app_users', 'All Organizational App Users'),
    ('groups', 'Select Notification Groups'),
)

STATUS = (
    ('active', 'Active'),
    ('inactive', 'Inactive')
)

EVENT_CHOICES = (
    ('sos', 'SOS'),
    ('all', 'All'),
    ('timer', 'Timer'),
    ('safe_walk', 'Safe WALK'),
)


class Contacts(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=255, null=False)
    country_code = models.CharField(max_length=5, choices=COUNTRY_CHOICES, default='+91', null=False)
    mobile = models.CharField(max_length=12, null=False)
    event_notification = models.CharField(max_length=255, choices=NOTIFY, default=None, blank=True, null=True)
    event_types = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='active')

    def __str__(self):
        return self.email

    def get_event_types(self):
        return self.event_types.split(',')

    def set_event_types(self, event_types_list):
        self.event_types = ','.join(event_types_list)

