from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Application(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Personal Information
    student_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100, blank=True)
    dob = models.DateField()
    email = models.EmailField()
    present_address = models.TextField()
    permanent_address = models.TextField(blank=True)
    telephone_residence = models.CharField(max_length=15, blank=True)
    telephone_mobile = models.CharField(max_length=15)
    allergies = models.TextField(blank=True)

    # Education
    x_board = models.CharField(max_length=100, blank=True)
    x_year = models.CharField(max_length=10, blank=True)
    x_percent = models.CharField(max_length=10, blank=True)

    xii_board = models.CharField(max_length=100, blank=True)
    xii_year = models.CharField(max_length=10, blank=True)
    xii_percent = models.CharField(max_length=10, blank=True)

    btech1_sem1 = models.CharField(max_length=10, blank=True)
    btech1_sem2 = models.CharField(max_length=10, blank=True)
    btech2_sem3 = models.CharField(max_length=10, blank=True)
    btech2_sem4 = models.CharField(max_length=10, blank=True)
    btech3_sem5 = models.CharField(max_length=10, blank=True)
    btech3_sem6 = models.CharField(max_length=10, blank=True)
    btech4_sem7 = models.CharField(max_length=10, blank=True)
    btech4_sem8 = models.CharField(max_length=10, blank=True)

    mtech1_sem1 = models.CharField(max_length=10, blank=True)
    mtech1_sem2 = models.CharField(max_length=10, blank=True)
    mtech2_sem3 = models.CharField(max_length=10, blank=True)
    mtech2_sem4 = models.CharField(max_length=10, blank=True)

    # Training
    course_name = models.CharField(max_length=100)
    semester = models.CharField(max_length=20)
    institute_name = models.CharField(max_length=200)
    training_duration = models.CharField(max_length=50)
    training_from = models.DateField()
    training_to = models.DateField()

    # File Uploads
    photograph = models.ImageField(upload_to='photographs/')
    cv_upload = models.FileField(upload_to='cvs/', null=True, blank=True)
    identification_doc = models.FileField(upload_to='ids/')
    signature_upload = models.ImageField(upload_to='signatures/')

    # Declaration
    declaration_date = models.DateField()
    photo_confirm = models.BooleanField(default=False)

    # Status and Timestamp
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    submitted_date = models.DateTimeField(auto_now_add=True)

    review_comments = models.TextField(blank=True, null=True)  # for rejected case


    def __str__(self):
        return f"{self.student_name} - {self.course_name} ({self.status})"