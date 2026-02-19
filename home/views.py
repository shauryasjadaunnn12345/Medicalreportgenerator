from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser, User
from .forms import YBOCSForm
from .models import DiagnosisResult

def ybocs_input(request):
    if request.method == "POST":
        form = YBOCSForm(request.POST)
        if form.is_valid():
            # Ensure all values are cast to int
            obsession_score = sum([
                int(form.cleaned_data['obsession_time']),
                int(form.cleaned_data['obsession_interference']),
                int(form.cleaned_data['obsession_distress']),
                int(form.cleaned_data['obsession_resistance']),
                int(form.cleaned_data['obsession_control']),
            ])

            compulsion_score = sum([
                int(form.cleaned_data['compulsion_time']),
                int(form.cleaned_data['compulsion_interference']),
                int(form.cleaned_data['compulsion_distress']),
                int(form.cleaned_data['compulsion_resistance']),
                int(form.cleaned_data['compulsion_control']),
            ])

            total_score = obsession_score + compulsion_score

            # Determine diagnosis
            if total_score >= 25:
                diagnosis_text = "Severe OCD"
            elif total_score >= 15:
                diagnosis_text = "Moderate OCD"
            else:
                diagnosis_text = "Mild OCD"

            # Save data based on user authentication
            if request.user.is_authenticated:
                user_profile = request.user
                OCDSymptoms.objects.create(
                    user_profile=user_profile,
                    obsession_score=obsession_score,
                    compulsion_score=compulsion_score
                )
                diagnosis = DiagnosisResult.objects.create(
                    user_profile=user_profile,
                    diagnosed_condition=diagnosis_text
                )
            else:
                # OCDSymptoms.objects.create(
                #     obsession_score=obsession_score,
                #     compulsion_score=compulsion_score
                # )
                diagnosis = DiagnosisResult.objects.create(
                    diagnosed_condition=diagnosis_text
                )
                # Save for anonymous user
                request.session['anon_diagnosis_id'] = diagnosis.id

            return redirect('home:results')
    else:
        form = YBOCSForm()

    return render(request, 'ybocs_input.html', {'form': form})


def diagnosis_results(request):
    diagnosis = None
    message = None

    if request.user.is_authenticated:
        diagnosis = DiagnosisResult.objects.filter(user_profile=request.user).last()
        if not diagnosis:
            message = "No diagnosis found yet."
    else:
        diagnosis_id = request.session.get('anon_diagnosis_id')
        if diagnosis_id:
            diagnosis = DiagnosisResult.objects.filter(id=diagnosis_id).first()
            if not diagnosis:
                message = "We couldn't find your session diagnosis result."
        else:
            message = "You haven’t taken any diagnosis yet."

    return render(request, 'tests.html', {
        'diagnosis': diagnosis,
        'message': message
    })

def daily_plan(request):
    return render(request, 'daily_plan.html')
def base_generic(request):
    return render(request,"base_generic.html")
   

def ocd_detail(request):
    return render(request, 'ocd_detail.html')
from django.shortcuts import render
from .forms import GAD7Form

from django.shortcuts import render, redirect
from .forms import GAD7Form
from .models import DiagnosisResult

def gad7_view(request):
    result = None
    diagnosis_text = None

    if request.method == 'POST':
        form = GAD7Form(request.POST)
        if form.is_valid():
            # Calculate the score based on form responses
            score = sum(int(form.cleaned_data[q]) for q in form.cleaned_data)

            # Determine the diagnosis based on the score
            if score <= 4:
                diagnosis_text = "Minimal anxiety"
            elif score <= 9:
                diagnosis_text = "Mild anxiety"
            elif score <= 14:
                diagnosis_text = "Moderate anxiety"
            else:
                diagnosis_text = "Severe anxiety"

            # Save the result to the DiagnosisResult model
            if request.user.is_authenticated:
                diagnosis = DiagnosisResult.objects.create(
                    user_profile=request.user,
                    diagnosed_condition=diagnosis_text
                )
            else:
                diagnosis = DiagnosisResult.objects.create(
                    diagnosed_condition=diagnosis_text
                )
                # Save the diagnosis ID for anonymous users
                request.session['anon_diagnosis_id'] = diagnosis.id

            return redirect('home:results')  # Redirect to results page
    else:
        form = GAD7Form()

    return render(request, 'gad.html', {'form': form, 'result': result})

def gad7(request):
    return render(request, 'gad.html')
def anxiety(request):
    return render(request, 'anxiety.html')

from django.shortcuts import render
from .forms import PHQ9Form

def phq9_view(request):
    result = None
    if request.method == 'POST':
        form = PHQ9Form(request.POST)
        if form.is_valid():
            # Calculate the total score by summing the selected values for all questions
            score = sum(int(form.cleaned_data[f'q{i}']) for i in range(1, 10))

            # Determine severity based on the total score
            if score <= 4:
                result = "Minimal Depression"
            elif score <= 9:
                result = "Mild Depression"
            elif score <= 14:
                result = "Moderate Depression"
            elif score <= 19:
                result = "Moderately Severe Depression"
            else:
                result = "Severe Depression"

            # Save diagnosis result
            if request.user.is_authenticated:
                diagnosis = DiagnosisResult.objects.create(
                    user_profile=request.user,
                    diagnosed_condition=result
                )
            else:
                diagnosis = DiagnosisResult.objects.create(
                    diagnosed_condition=result
                )
                request.session['anon_diagnosis_id'] = diagnosis.id

            return redirect('home:results')  # Redirect to results page
    else:
        form = PHQ9Form()

    return render(request, 'phq9_test.html', {'form': form, 'result': result})

def phq9(request):
    return render(request,"phq9_test.html")
def dep(request):
    return render(request,"depression.html")
from django.shortcuts import render, redirect
from .forms import MDQForm
from .models import DiagnosisResult  # Assuming you have a model for saving diagnosis results

def mdq_view(request):
    result = None
    if request.method == 'POST':
        form = MDQForm(request.POST)
        if form.is_valid():
            # Check if the user answered "Yes" to at least 7 questions
            yes_answers = sum(1 for i in range(1, 14) if form.cleaned_data[f'q{i}'] == 'yes')
            if yes_answers >= 7 and form.cleaned_data['symptoms_occurred_together'] == 'yes':
                result = "Possible bipolar disorder – further assessment recommended"
            else:
                result = "Bipolar disorder unlikely"
            
            # Severity of the symptoms
            severity = form.cleaned_data['severity']
            
            # Record the result to the database (if the user is logged in or anonymous)
            diagnosis_text = result + f" (Severity: {severity})"
            if request.user.is_authenticated:
                diagnosis = DiagnosisResult.objects.create(
                    user_profile=request.user,
                    diagnosed_condition=diagnosis_text
                )
            else:
                diagnosis = DiagnosisResult.objects.create(
                    diagnosed_condition=diagnosis_text
                )
                # Save the diagnosis ID for anonymous users
                request.session['anon_diagnosis_id'] = diagnosis.id

            return redirect('home:results')  # Redirect to results page
    else:
        form = MDQForm()

    return render(request, 'mdq_test.html', {'form': form, 'result': result})

def mdq(request):
    return render(request,"mdq_test.html")
def bipolar(request):
    return render(request,"bipolar.html")
from django.shortcuts import render, redirect
from .forms import PCL5Form
from .models import DiagnosisResult

def pcl5_view(request):
    result = None
    if request.method == 'POST':
        form = PCL5Form(request.POST)
        if form.is_valid():
            # Calculate total score by summing responses (1-4 scale for each question)
            total_score = sum(int(form.cleaned_data[f'q{i}']) for i in range(1, 21))

            # Determine the severity of PTSD based on total score
            if total_score <= 19:
                result = "Mild PTSD"
            elif total_score <= 34:
                result = "Moderate PTSD"
            elif total_score <= 49:
                result = "Severe PTSD"
            else:
                result = "Very Severe PTSD"
            
            # Record the result to the database (if the user is logged in or anonymous)
            diagnosis_text = f"PTSD Diagnosis: {result} (Total Score: {total_score})"
            if request.user.is_authenticated:
                diagnosis = DiagnosisResult.objects.create(
                    user_profile=request.user,
                    diagnosed_condition=diagnosis_text
                )
            else:
                diagnosis = DiagnosisResult.objects.create(
                    diagnosed_condition=diagnosis_text
                )
                # Save the diagnosis ID for anonymous users
                request.session['anon_diagnosis_id'] = diagnosis.id

            return redirect('home:results')  # Redirect to results page
    else:
        form = PCL5Form()

    return render(request, 'pcl5_test.html', {'form': form, 'result': result})
def pcl5(request):
    return render(request,"pcl5_test.html")
def ptsd(request):
    return render(request,"ptsd.html")
from django.shortcuts import render, redirect
from .forms import SchizophreniaTestForm
from home.models import DiagnosisResult

def schizophrenia_test_view(request):
    result = None
    if request.method == 'POST':
        form = SchizophreniaTestForm(request.POST)
        if form.is_valid():
            total_score = sum(int(form.cleaned_data[f'q{i}']) for i in range(1, 11))

            if total_score >= 30:
                result = "High likelihood of schizophrenia – further evaluation is strongly recommended."
            elif 20 <= total_score < 30:
                result = "Moderate symptoms – professional consultation is advised."
            else:
                result = "Low likelihood of schizophrenia – symptoms may not indicate the disorder."

            # Save to database
            if request.user.is_authenticated:
                diagnosis = DiagnosisResult.objects.create(
                    user_profile=request.user,
                    diagnosed_condition=f"Schizophrenia Test Result: {result}"
                )
            else:
                diagnosis = DiagnosisResult.objects.create(
                    diagnosed_condition=f"Schizophrenia Test Result: {result}"
                )
                request.session['anon_diagnosis_id'] = diagnosis.id

            return redirect('home:results')  # Adjust this if your result URL is different
    else:
        form = SchizophreniaTestForm()

    return render(request, 'schizophrenia_test.html', {'form': form, 'result': result})
def sssc(request):
    return render(request,"schizophrenia_test.html")
def schizophrenia(request):
    return render(request,"schizophrenia_info.html")
from django.shortcuts import render, redirect
from .forms import ASRSForm
from home.models import DiagnosisResult  # Adjust based on your model path

def asrs_view(request):
    result = None

    if request.method == 'POST':
        form = ASRSForm(request.POST)
        if form.is_valid():
            # Scoring Part A (questions 1–6)
            responses = [form.cleaned_data[f'q{i}'] for i in range(1, 7)]
            positive_count = sum(1 for r in responses if r in ['often', 'very_often'])

            if positive_count >= 4:
                result = "High likelihood of ADHD – further evaluation is recommended."
            else:
                result = "Unlikely to have ADHD based on this screening."

            # Save to database
            diagnosis_text = f"ASRS Result: {result}"
            if request.user.is_authenticated:
                DiagnosisResult.objects.create(
                    user_profile=request.user,
                    diagnosed_condition=diagnosis_text
                )
            else:
                diagnosis = DiagnosisResult.objects.create(
                    diagnosed_condition=diagnosis_text
                )
                request.session['anon_diagnosis_id'] = diagnosis.id

            return redirect('home:results')

    else:
        form = ASRSForm()

    return render(request, 'asrs_test.html', {'form': form, 'result': result})
def asrs(request):
    return render(request,"asrs_test.html")
def adhd(request):
    return render(request,"adhd.html")
from django.shortcuts import render
from .forms import AQTestForm

from django.shortcuts import render, redirect
from .forms import AQTestForm
from .models import DiagnosisResult  # Make sure to have a model to store the diagnosis

def aq_test_view(request):
    result = None

    if request.method == 'POST':
        form = AQTestForm(request.POST)
        if form.is_valid():
            # Scoring AQ Test - Summing up the answers (lower score indicating more autistic traits)
            responses = [form.cleaned_data[f'q{i}'] for i in range(1, 11)]  # Adjust range based on your questions
            score = sum(int(r) for r in responses)  # Total score calculation

            # Determine result based on score
            if score >= 30:  # You can adjust this threshold as needed
                result = "High likelihood of Autism Spectrum Disorder – further evaluation is recommended."
            else:
                result = "Unlikely to have Autism Spectrum Disorder based on this screening."

            # Save the diagnosis to the database (if the user is authenticated)
            diagnosis_text = f"AQ Test Result: {result}"
            if request.user.is_authenticated:
                DiagnosisResult.objects.create(
                    user_profile=request.user,
                    diagnosed_condition=diagnosis_text
                )
            else:
                diagnosis = DiagnosisResult.objects.create(
                    diagnosed_condition=diagnosis_text
                )
                request.session['anon_diagnosis_id'] = diagnosis.id  # Save for non-authenticated users

            return redirect('home:results')  # Redirect to the result page (you may change the URL name)

    else:
        form = AQTestForm()

    return render(request, 'aq_test.html', {'form': form, 'result': result})
def aq(request):
    return render(request,'aq_test.html')
def autism(request):
    return render(request,"autism.html")

from .forms import PanicDisorderForm
from .models import DiagnosisResult
def panic_test_view(request):
    result = None

    if request.method == 'POST':
        form = PanicDisorderForm(request.POST)
        if form.is_valid():
            responses = [form.cleaned_data[f'q{i}'] for i in range(1, 8)]
            positive_count = sum(1 for r in responses if r in ['often', 'very_often'])

            if positive_count >= 4:
                result = "Your responses indicate a potential for Panic Disorder. Please consult a professional for a full evaluation."
            else:
                result = "Your responses suggest it's unlikely you have Panic Disorder, but stay mindful of your mental health."

            # Save to database
            diagnosis_text = f"Panic Disorder Test Result: {result}"
            if request.user.is_authenticated:
                DiagnosisResult.objects.create(
                    user_profile=request.user,
                    diagnosed_condition=diagnosis_text
                )
            else:
                diagnosis = DiagnosisResult.objects.create(
                    diagnosed_condition=diagnosis_text
                )
                request.session['anon_diagnosis_id'] = diagnosis.id

            return redirect('home:results')

    else:
        form = PanicDisorderForm()

    return render(request, 'panic_test.html', {'form': form, 'result': result})
def pdss(request):
    return render(request,"panic_test.html")
def panic(request):
    return render(request,"panic.html")
from django.shortcuts import render, redirect
from .forms import SleepDisorderForm
from .models import DiagnosisResult

from django.shortcuts import render, redirect
from .forms import SleepDisorderForm
from .models import DiagnosisResult

def sleep_test_view(request):
    result = None

    if request.method == 'POST':
        form = SleepDisorderForm(request.POST)
        if form.is_valid():
            # Collect responses from 10 questions
            responses = [form.cleaned_data[f'q{i}'] for i in range(1, 11)]

            # Count answers that indicate concern
            positive_count = sum(1 for r in responses if r in ['often', 'very_often'])

            # Basic interpretation
            if positive_count >= 5:
                result = "Your answers suggest a potential sleep disorder. It's recommended to speak with a healthcare professional."
            else:
                result = "Your responses do not strongly indicate a sleep disorder. Maintain healthy sleep habits and monitor any changes."

            # Save to database
            diagnosis_text = f"Sleep Disorder Test Result: {result}"
            if request.user.is_authenticated:
                DiagnosisResult.objects.create(
                    user_profile=request.user,
                    diagnosed_condition=diagnosis_text
                )
            else:
                diagnosis = DiagnosisResult.objects.create(
                    diagnosed_condition=diagnosis_text
                )
                request.session['anon_diagnosis_id'] = diagnosis.id

            return redirect('home:results')
    else:
        form = SleepDisorderForm()

    return render(request, 'sleep_test.html', {'form': form, 'result': result})
def sleeptest(request):
    return render(request,"sleep_test.html")
def sleep(request):
    return render(request,"sleep.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def login(request):
    return render(request,"login.html")
def signup(request):
    return render(request,"signup.html")



from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')

        # Allow login with username or email
        user = authenticate(request, username=username_or_email, password=password)
        if user is None:
            try:
                from django.contrib.auth.models import User
                user_obj = User.objects.get(email=username_or_email)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                pass

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')  # Replace 'home' with your homepage URL name
        else:
            messages.error(request, "Invalid login credentials.")
    
    return render(request, 'login.html')
    

def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            otp_entry, _ = EmailOTP.objects.get_or_create(email=email)
            otp_entry.generate_otp()

            send_mail(
                subject='MindCare Password Reset OTP',
                message=f'Your password reset OTP is {otp_entry.otp}',
                from_email='noreply@mindcare.com',
                recipient_list=[email],
                fail_silently=False,
            )
            request.session['reset_email'] = email
            return redirect('reset_password_otp')
        except User.DoesNotExist:
            messages.error(request, "Email not found.")

    return render(request, 'forgot_password.html')
def send_otp_email(user_email, otp):
    """Send the OTP to the user's email."""
    subject = "Your OTP for MindCare Signup"
    message = f"Your OTP is {otp}. Please enter it to complete your signup process."
    from_email = "no-reply@mindcare.com"  # Replace with your actual email

    send_mail(subject, message, from_email, [user_email])

def reset_password_otp(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        email = request.session.get('reset_email')

        try:
            otp_entry = EmailOTP.objects.get(email=email)
            if otp_entry.otp == otp:
                if new_password == confirm_password and len(new_password) >= 8:
                    user = User.objects.get(email=email)
                    user.set_password(new_password)
                    user.save()
                    otp_entry.delete()
                    del request.session['reset_email']
                    messages.success(request, "Password reset successful!")
                    return redirect('login')
                else:
                    messages.error(request, "Passwords must match and be at least 8 characters.")
            else:
                messages.error(request, "Invalid OTP.")
        except EmailOTP.DoesNotExist:
            messages.error(request, "OTP is invalid or expired.")

    return render(request, 'reset_password_otp.html')
def forgotpassword(request):
    return render(request,"forgot_password.html")
def resetpassword(request):
    return render(request,"reset_password_otp.html")
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomSignupForm
from .models import EmailOTP
from .utils import send_otp_email
from django.contrib.auth import login


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .models import EmailOTP
from .forms import CustomSignupForm
from .utils import send_otp_email  # Adjust if you named this differently
import random
from random import randint
from datetime import timedelta
from django.utils import timezone
def signup_view(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # Store form data in session
            request.session['signup_data'] = {
                'email': email,
                'username': username,
                'password': password,
            }

            # Generate and send OTP
            email_otp, created = EmailOTP.objects.get_or_create(email=email)
            email_otp.generate_otp()
            send_otp_email(email, email_otp.otp)
            messages.success(request, 'A verification OTP has been sent to your email.')
            
            # Redirect to verify_otp with email in query param
            return redirect(f"{reverse('verify_otp')}?email={email}")
    else:
        form = CustomSignupForm()

    return render(request, 'signup.html', {'form': form})


from django.contrib.auth import get_user_model

User = get_user_model()

def verify_otp(request):
    if request.method == "POST":
        email = request.POST.get("email")
        otp_input = request.POST.get("otp")

        try:
            email_otp = EmailOTP.objects.get(email=email)
        except EmailOTP.DoesNotExist:
            return render(request, "verify_otp.html", {"error": "OTP not found.", "email": email})

        if email_otp.is_otp_expired():
            return render(request, "verify_otp.html", {"error": "OTP expired. Request a new one.", "email": email})

        if email_otp.otp == otp_input:
            # Check if user exists
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                # Create user from session data
                signup_data = request.session.get('signup_data')
                if signup_data and signup_data['email'] == email:
                    user = User.objects.create_user(
                        username=signup_data['username'],
                        email=email,
                        password=signup_data['password']
                    )
                else:
                    return render(request, "verify_otp.html", {"error": "Session expired or invalid.", "email": email})

            # Log in user
            login(request, user)
            messages.success(request, "You have been logged in successfully.")
            return redirect("home")

        else:
            return render(request, "verify_otp.html", {"error": "Invalid OTP.", "email": email})

    # For GET request: get email from URL query param
    email = request.GET.get("email", "")
    return render(request, "verify_otp.html", {"email": email})
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home')  # Or redirect to your login page if needed


def resend_otp(request):
    email = request.POST.get('email')
    try:
        email_otp = EmailOTP.objects.get(email=email)
        email_otp.generate_otp()  # Regenerate OTP
        send_otp_email(email, email_otp.otp)  # Send new OTP to user email
        messages.success(request, 'A new OTP has been sent to your email.')
    except EmailOTP.DoesNotExist:
        messages.error(request, 'This email is not registered.')

    return redirect('verify_otp')
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views import View

class SitemapView(View):
    def get(self, request, *args, **kwargs):
        # Render the sitemap.xml using the template
        sitemap_content = render_to_string('sitemap.xml', {})
        return HttpResponse(sitemap_content, content_type="application/xml")

class RobotsView(View):
    def get(self, request, *args, **kwargs):
        # Render the robots.txt using the template
        robots_content = render_to_string('robots.txt', {})
        return HttpResponse(robots_content, content_type="text/plain")

def home(request):
    return render(request,"base_generic.html")
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the contact message to the database

            # Optionally, send an email notification or perform additional actions here

            # Success message
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Redirect back to the contact page after successful submission
        else:
            messages.error(request, 'There was an error with your submission. Please try again.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
