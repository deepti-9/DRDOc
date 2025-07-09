from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from HR.models import TrainingApplication
from django.contrib import messages
import json

def parse_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

# to check registered applicant 
@login_required(login_url='login_applicant')
def applicant_dashboard(request):
    user = request.user

    # Fetch latest 1 applications by current user
    recent_applications = TrainingApplication.objects.filter(applicant=user).order_by('-submitted_date')[:1]
    # sending user data to html page to show personalise messages 
    context = {
        'username': user.username,
        'recent_applications': recent_applications
    }

    return render(request, 'applications/applicant_dashboard.html', context)


#  API endpoint to get applications via JavaScript
@login_required
def get_recent_applications_json(request):
    user = request.user
    applications = TrainingApplication.objects.filter(applicant=user).order_by('-submitted_date')[:1]

    app_data = [{
        'studentName': app.student_name,
        'courseName': app.course_name,
        'submittedDate': app.submitted_date.strftime('%Y-%m-%d'),
        'status': app.status
    } for app in applications]

    return JsonResponse(app_data, safe=False)

@login_required

def application_form_view(request):
    if request.method == 'POST':
        data = request.POST
        files = request.FILES

        app = TrainingApplication(
            applicant=request.user,
            student_name=data.get('studentName'),
            father_name=data.get('fatherName'),
            father_occupation=data.get('fatherOccupation'),
            dob=data.get('dob'),
            email=data.get('email'),
            present_address=data.get('presentAddress'),
            permanent_address=data.get('permanentAddress'),
            telephone_residence=data.get('telephoneResidence'),
            telephone_mobile=data.get('telephoneMobile'),
            allergies=data.get('allergies'),

            # Education
            x_board= data.get('x_board'),
            x_year= data.get('x_year'),
            x_percent= data.get('x_percent'),
            xii_board= data.get('xii_board'),
            xii_year= data.get('xii_year'),
            xii_percent= data.get('xii_percent'),

            btech1_sem1=data.get('btech1_sem1'),
            btech1_sem2=data.get('btech1_sem2'),
            btech2_sem3= parse_float(data.get('btech2_sem3')),
            btech2_sem4= parse_float(data.get('btech2_sem4')),
            btech3_sem5= parse_float(data.get('btech3_sem5')),
            btech3_sem6= parse_float(data.get('btech3_sem6')),
            btech4_sem7= parse_float(data.get('btech4_sem7')),
            btech4_sem8= parse_float(data.get('btech4_sem8')),
            mtech1_sem1= parse_float(data.get('mtech1_sem1')),
            mtech1_sem2= parse_float(data.get('mtech1_sem2')),
            mtech2_sem3= parse_float(data.get('mtech2_sem3')),
            mtech2_sem4= parse_float(data.get('mtech2_sem4')),

            # Training
            course_name=data.get('courseName'),
            semester=data.get('semester'),
            institute_name=data.get('instituteName'),
            training_duration=data.get('trainingDuration'),
            training_from=data.get('trainingFrom'),
            training_to=data.get('trainingTo'),

            # Files
            photograph=files.get('photograph'),
            resume = files.get('cvUpload'),
            id_proof = files.get('identificationDoc'),
            signature_upload=files.get('signatureUpload'),

            declaration_date=data.get('declarationDate')
        )

        app.save()
        messages.success(request, "Application submitted successfully.")
        return redirect('applicant_dashboard')

    return render(request, 'applications/application_form.html')



@login_required
def application_status_view(request):
    user = request.user
    applications = TrainingApplication.objects.filter(applicant=user).order_by('-submitted_date')

    # Prepare list of dicts
    apps_data = []
    for app in applications:
        apps_data.append({
            "studentName": app.student_name,
            "courseName": app.course_name,
            "instituteName": getattr(app, "institute_name", ""),
            "trainingDuration": getattr(app, "training_duration", ""),
            "trainingFrom": app.training_from.strftime("%Y-%m-%d") if app.training_from else "",
            "trainingTo": app.training_to.strftime("%Y-%m-%d") if app.training_to else "",
            "submittedDate": app.submitted_date.strftime("%Y-%m-%d"),
            "status": app.status,
            "reviewComments": getattr(app, "review_comments", "")
        })

        context = {
            "username": request.user.username,
            "applications_json": json.dumps(apps_data)  
        }
    return render(request, "applications/application_status.html", context)