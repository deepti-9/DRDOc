from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import HRProfile
from django.urls import reverse



from django.shortcuts import render
def role_selection(request):
    return render(request, 'role_based_reg/RoleSelection.html')


def login_applicant(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
          
            return redirect('applicant_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'role_based_reg/login-applicant.html')

def login_hr(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('hr_dashboard'))  
        else:
            # Invalid credentials
            messages.error(request, 'Invalid username or password')

    return render(request, 'role_based_reg/login-hr.html')

def register_applicant(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'role_based_reg/register-applicant.html')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, 'role_based_reg/register-applicant.html')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return render(request, 'role_based_reg/register-applicant.html')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        messages.success(request, "Registration successful! Please login.")
        return redirect('login_applicant')

    return render(request, 'role_based_reg/register-applicant.html')

def register_hr(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        employee_id = request.POST.get('employee_id')
        department = request.POST.get('department')
        designation = request.POST.get('designation')
        reporting_manager = request.POST.get('reporting_manager')
        experience = request.POST.get('years_of_experience')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        terms = request.POST.get('terms')

        id_proof = request.FILES.get('id_proof')
        auth_letter = request.FILES.get('authorization_letter')

        # Validate terms
        if not terms:
            messages.error(request, "You must accept the terms and conditions.")
            return render(request, 'role_based_reg/register-hr.html')

        # Validate passwords
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'role_based_reg/register-hr.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'role_based_reg/register-hr.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'role_based_reg/register-hr.html')

        # Create Django user
        try:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )

            # Create HR profile (custom model)
            HRProfile.objects.create(
                user=user,
                phone_number=phone_number,
                employee_id=employee_id,
                department=department,
                designation=designation,
                reporting_manager=reporting_manager,
                years_of_experience=experience,
                id_proof=id_proof,
                authorization_letter=auth_letter
            )

            messages.success(request, "HR registration successful. You can now log in.")
            return redirect('login_hr')  # redirect to login page

        except Exception as e:
            messages.error(request, f"Registration failed: {str(e)}")
            return render(request, 'role_based_reg/register-hr.html')

    return render(request, 'role_based_reg/register-hr.html')

 