# Generated by Django 5.2.3 on 2025-07-04 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('course_name', models.CharField(max_length=100)),
                ('institute_name', models.CharField(max_length=200)),
                ('training_duration', models.IntegerField()),
                ('training_from', models.DateField()),
                ('training_to', models.DateField()),
                ('submitted_date', models.DateField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_phone', models.CharField(max_length=15)),
                ('cgpa', models.FloatField(blank=True, null=True)),
                ('semester', models.CharField(blank=True, max_length=20)),
                ('branch', models.CharField(blank=True, max_length=100)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
                ('marksheet', models.FileField(blank=True, null=True, upload_to='marksheets/')),
                ('bonafide_certificate', models.FileField(blank=True, null=True, upload_to='bonafides/')),
                ('id_proof', models.FileField(blank=True, null=True, upload_to='id_proofs/')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10)),
                ('review_comments', models.TextField(blank=True)),
                ('review_date', models.DateField(blank=True, null=True)),
                ('reviewed_by', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
