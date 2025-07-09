from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import TrainingApplication
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import date

def hr_dashboard(request):
    return render(request, 'HR/hr_dashboard.html', {'username': request.user.username})
    
def get_applications(request):
    print("HR APPLICATION VIEW LOADED")
    applications = TrainingApplication.objects.all().order_by('-submitted_date')

    data = []
    for app in applications:
        data.append({
            'id': app.id,
            'studentName': app.student_name,
            'courseName': app.course_name,
            'instituteName': app.institute_name,
            'trainingDuration': app.training_duration,
            'trainingFrom': app.training_from,
            'trainingTo': app.training_to,
            'submittedDate': app.submitted_date,
            'email': app.email,
            'mobilePhone': app.telephone_mobile, 
            'status': app.status,
            'reviewComments': app.review_comments,
            'reviewDate': app.review_date,
        })
    return JsonResponse(data, safe=False)

@csrf_exempt
def review_application(request):
    if request.method == 'POST':
        print(">>> REVIEW ENDPOINT HIT")
        data = json.loads(request.body)
        print("Received Data:", data) 
        app_id = data.get('id')
        action = data.get('action')
        comments = data.get('comments')

        app = get_object_or_404(TrainingApplication, id=app_id)
        if action == 'approve':
            app.status = 'approved'
        elif action == 'reject':
            app.status = 'rejected'
        else:
            return JsonResponse({'success': False, 'message': 'Invalid action'})
        
        print("Review Action:", action, "| New Status in DB:", app.status)
        app.review_comments = comments
        app.review_date = date.today()
        app.reviewed_by = request.user.username if request.user.is_authenticated else "System"
        app.save()

        return JsonResponse({'success': True, 'message': f"Application {app.status}."})
    return JsonResponse({'success': False, 'message': "Invalid request."})

