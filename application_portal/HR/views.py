from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import TrainingApplication
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import date

def hr_dashboard(request):
    return render(request, 'HR/hr_dashboard.html', {'username': request.user.username})

def get_applications(request):
    apps = TrainingApplication.objects.all().values()
    return JsonResponse(list(apps), safe=False)

@csrf_exempt
def review_application(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        app_id = data.get('id')
        action = data.get('action')
        comments = data.get('comments')

        app = get_object_or_404(TrainingApplication, id=app_id)
        app.status = action
        app.review_comments = comments
        app.review_date = date.today()
        app.reviewed_by = request.user.username
        app.save()

        return JsonResponse({'success': True, 'message': f"Application {action}d."})
    return JsonResponse({'success': False, 'message': "Invalid request."})

