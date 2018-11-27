from django.db import models

# Create your models here.
ROLE_CHOICES = (
    ('admin', 'admin'),
    ('regular', 'regular'),
)


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=8, choices=ROLE_CHOICES)

    class Meta:
        db_table = "team"
