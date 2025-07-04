from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class HRProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    employee_id = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    reporting_manager = models.CharField(max_length=100)
    years_of_experience = models.CharField(max_length=20)

    id_proof = models.FileField(upload_to='hr/id_proofs/')
    authorization_letter = models.FileField(upload_to='hr/auth_letters/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.department})"

