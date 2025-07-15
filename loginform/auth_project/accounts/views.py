import re
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import IntegrityError
from django.contrib.auth import get_user_model

User = get_user_model()  # This ensures flexibility with custom user models

# ✅ Home view
def home(request):
    return render(request, 'home.html')


# ✅ Password strength checker
def is_strong_password(password):
    """
    Checks password strength:
    - At least 8 characters
    - Includes uppercase letter
    - Includes lowercase letter
    - Includes number
    - Includes special character (@$!%*?&)
    """
    if (
        len(password) < 8 or
        not re.search(r'[A-Z]', password) or
        not re.search(r'[a-z]', password) or
        not re.search(r'\d', password) or
        not re.search(r'[@$!%*?&]', password)
    ):
        return False
    return True


# ✅ Signup view
def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')

        # ✅ Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered.")
            return redirect('signup')

        # ✅ Validate password strength
        if not is_strong_password(password):
            messages.error(request, "Password must be at least 8 characters long, include an uppercase letter, a lowercase letter, a number, and a special character like @, $, !, %, *, ?, &.")
            return redirect('signup')

        try:
            # ✅ Create the user
            User.objects.create_user(email=email, password=password, username=username)
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('login')
        except IntegrityError:
            messages.error(request, "An error occurred while creating your account.")
            return redirect('signup')

    return render(request, 'signup.html')


# ✅ Login view
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # ✅ Authenticate user
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)

            # ✅ Generate JWT access token
            refresh = RefreshToken.for_user(user)

            return render(request, 'dashboard.html', {
                'access': str(refresh.access_token)
            })
        else:
            return render(request, 'login.html', {
                'error': 'Invalid email or password.'
            })

    return render(request, 'login.html')


# ✅ Dashboard view (only accessible after login)
@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'dashboard.html', {
        'user': request.user
    })


# ✅ Logout view
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')
