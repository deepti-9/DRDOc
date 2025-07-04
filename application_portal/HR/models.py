from django.db import models

# Create your models here.
class TrainingApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    student_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    institute_name = models.CharField(max_length=200)
    training_duration = models.IntegerField()  # in months
    training_from = models.DateField()
    training_to = models.DateField()
    submitted_date = models.DateField(auto_now_add=True)
    email = models.EmailField()
    mobile_phone = models.CharField(max_length=15)

    # New Academic Fields
    cgpa = models.FloatField(null=True, blank=True)
    semester = models.CharField(max_length=20, blank=True)
    branch = models.CharField(max_length=100, blank=True)
    
    # File Uploads (ensure MEDIA setup is done in settings.py)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    marksheet = models.FileField(upload_to='marksheets/', null=True, blank=True)
    bonafide_certificate = models.FileField(upload_to='bonafides/', null=True, blank=True)
    id_proof = models.FileField(upload_to='id_proofs/', null=True, blank=True)

    # Status and Review
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    review_comments = models.TextField(blank=True)
    review_date = models.DateField(null=True, blank=True)
    reviewed_by = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.student_name

