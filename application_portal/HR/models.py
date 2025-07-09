from django.db import models
from django.contrib.auth.models import User

class TrainingApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    applicant = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name="applications")

    student_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100, blank=True)
    father_occupation = models.CharField(max_length=100, blank=True)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField()
    present_address = models.TextField(blank=True)
    permanent_address = models.TextField(blank=True)
    telephone_residence = models.CharField(max_length=15, blank=True)
    telephone_mobile = models.CharField(max_length=15)

    allergies = models.TextField(blank=True)

    # Education Details
    x_board = models.CharField(max_length=100, blank=True)
    x_year = models.CharField(max_length=10, blank=True)
    x_percent = models.FloatField(null=True, blank=True)
    xii_board = models.CharField(max_length=100, blank=True)
    xii_year = models.CharField(max_length=10, blank=True)
    xii_percent = models.FloatField(null=True, blank=True)

    btech1_sem1 = models.FloatField(null=True, blank=True)
    btech1_sem2 = models.FloatField(null=True, blank=True)
    btech2_sem3 = models.FloatField(null=True, blank=True)
    btech2_sem4 = models.FloatField(null=True, blank=True)
    btech3_sem5 = models.FloatField(null=True, blank=True)
    btech3_sem6 = models.FloatField(null=True, blank=True)
    btech4_sem7 = models.FloatField(null=True, blank=True)
    btech4_sem8 = models.FloatField(null=True, blank=True)
    mtech1_sem1 = models.FloatField(null=True, blank=True)
    mtech1_sem2 = models.FloatField(null=True, blank=True)
    mtech2_sem3 = models.FloatField(null=True, blank=True)
    mtech2_sem4 = models.FloatField(null=True, blank=True)

    # Training
    course_name = models.CharField(max_length=100)
    semester = models.CharField(max_length=20, blank=True)
    institute_name = models.CharField(max_length=200)
    training_duration = models.IntegerField()
    training_from = models.DateField()
    training_to = models.DateField()

    # File Uploads
    resume = models.FileField(upload_to='cvUpload/', null=True, blank=True)
    id_proof = models.FileField(upload_to='identificationDoc/', null=True, blank=True)
    photograph = models.FileField(upload_to='photos/', null=True, blank=True)
    signature_upload = models.FileField(upload_to='signatures/', null=True, blank=True)
    
    declaration_date = models.DateField(null=True, blank=True)
    submitted_date = models.DateField(auto_now_add=True)
    # Status and Review
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    review_comments = models.TextField(blank=True)
    review_date = models.DateField(null=True, blank=True)
    reviewed_by = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.student_name} - {self.course_name}"
    



