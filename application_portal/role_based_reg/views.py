from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.models import User


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
            # Redirect to applicant dashboard (create later)
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
            return redirect('hr_dashboard')  # replace with your actual dashboard URL name
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
    return render(request, 'role_based_reg/register-hr.html')

