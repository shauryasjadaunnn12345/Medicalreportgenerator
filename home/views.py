import os
import requests
import re  
from io import BytesIO
import base64
from dotenv import load_dotenv
from django.shortcuts import render
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from django.shortcuts import render
from .forms import MedicalImageForm
from django.conf import settings
import PyPDF2
from django.contrib.auth.decorators import login_required
from .forms import LabReportForm
from django.shortcuts import  redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login
from dotenv import load_dotenv

from .forms import ContactForm
TEMP_DIR = os.path.join(settings.MEDIA_ROOT, "temp")
os.makedirs(TEMP_DIR, exist_ok=True)
import json
import requests

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.conf import settings
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
import environ


from django.conf import settings

from django.contrib.auth.models import User
def home(request):
    return render(request,"home.html")
def aboutdisplay(request):
    return render(request,"about.html")
def ads(request):
    return render(request,'ads.txt')
from datetime import date

def privacy_policy(request):
    return render(request, "privacy_policy.html", {"today": date.today()})
def sitemap(request):
    return render(request, "sitemap.xml")
def robots(request):
    return render(request, "robots.txt")

def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            # Optional: Send an email notification
            send_mail(
                subject="New Contact Message",
                message=f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}",
                from_email=form.cleaned_data['email'],
                recipient_list=["support@wrapdoctorsai.com"],  # Change to your email
            )

            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")  # Redirect to avoid re-submission
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re
from .models import CustomUser  # Ensure you have a custom user model

# Function to check password strength
def is_strong_password(password):
    """Check if password is strong."""
    return (
        len(password) >= 8 and
        re.search(r'[A-Z]', password) and  # At least one uppercase letter
        re.search(r'[a-z]', password) and  # At least one lowercase letter
        re.search(r'\d', password) and  # At least one number
        re.search(r'[!@#$%^&*(),.?":{}|<>]', password)  # At least one special character
    )

def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validate email format
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Invalid email format!")
            return redirect('signup')

        # Check if email or username already exists
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect('signup')
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken!")
            return redirect('signup')

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        # Check password strength
        if not is_strong_password(password1):
            messages.error(request, "Password must be at least 8 characters long and include an uppercase letter, lowercase letter, number, and special character!")
            return redirect('signup')

        # Create user but keep inactive until email verification
        user = CustomUser.objects.create_user(username=username, email=email, password=password1)
        user.is_active = False
        user.save()

        # Generate and send OTP
        otp = get_random_string(6, '0123456789')
        request.session['otp'] = otp  # Store OTP in session
        request.session['email'] = email  # Store email in session

        send_mail(
            'Your Verification OTP',
            f'Your OTP is {otp}. Enter this to verify your email.',
            'noreply@yourdomain.com',
            [email],
            fail_silently=False,
        )

        return redirect('verify_email')

    return render(request, 'signup.html')


def verify_email_view(request):
    email = request.session.get('email')
    if not email:
        messages.error(request, "Session expired. Please sign up again.")
        return redirect('signup')

    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        session_otp = request.session.get('otp')

        if session_otp and entered_otp == session_otp:
            try:
                user = CustomUser.objects.get(email=email)
                user.is_active = True  # Activate account
                user.save()

                # Remove OTP and email from session
                del request.session['otp']
                del request.session['email']

                messages.success(request, "Email verified! You can now log in.")
                return redirect('login')
            except CustomUser.DoesNotExist:
                messages.error(request, "User not found. Please sign up again.")
                return redirect('signup')
        else:
            messages.error(request, "Invalid OTP! Please try again.")

    return render(request, 'verify_email.html', {'email': email})


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')  # Redirect to home after login
            else:
                messages.error(request, "Please verify your email first!")
                return redirect('verify_email')
        else:
            messages.error(request, "Invalid username or password!")  # Error message

    return render(request, 'login.html')  # Ensure the template is reloaded

from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.shortcuts import redirect
from django.contrib import messages
from .models import CustomUser

def resend_otp_view(request):
    email = request.session.get('email')

    if not email:
        messages.error(request, "Session expired! Please sign up again.")
        return redirect('signup')

    if CustomUser.objects.filter(email=email).exists():
        otp = get_random_string(6, '0123456789')
        otp_storage[email] = otp  # Store new OTP

        send_mail(
            'Your New Verification OTP',
            f'Your new OTP is {otp}. Enter this to verify your email.',
            'noreply@yourdomain.com',
            [email],
            fail_silently=False,
        )

        messages.success(request, "A new OTP has been sent to your email.")
        return redirect('verify_email')

    messages.error(request, "User not found.")
    return redirect('signup')
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('/')  # Redirect to home after logout

load_dotenv()


API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {settings.OPENROUTER_API_KEY}", "Content-Type": "application/json"}

def get_medical_diagnosis(patient_name, age, gender, symptoms):
    """Generates AI-based diagnosis, treatment, and medicine prescription."""
    prompt = f"""
    Patient Details:
    - Name: {patient_name}
    - Age: {age}
    - Gender: {gender}
    - Symptoms: {symptoms}
    
    Provide a structured medical report in the following format:
    Diagnosis: <diagnosis_text>
    Treatment Plan: <treatment_plan_text>
    Medicines: <medicines_text>
    Additional Notes: <additional_notes_text>
    Follow-up: <follow_up_text>
    """

    payload = {
        "model": "mistralai/Mistral-7B-Instruct",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        data = response.json()

        diagnosis_text = data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()

        print("AI Response:", diagnosis_text)  # Debugging

        if not diagnosis_text:
            return {
                "Diagnosis": "⚠️ AI did not provide a diagnosis.",
                "Treatment Plan": "N/A",
                "Medicines": "N/A",
                "Additional Notes": "N/A",
                "Follow-up": "N/A",
            }

        sections = {
            "Diagnosis": re.search(r"Diagnosis:\s*(.+)", diagnosis_text),
            "Treatment Plan": re.search(r"Treatment Plan:\s*(.+)", diagnosis_text),
            "Medicines": re.search(r"Medicines:\s*(.+)", diagnosis_text),
            "Additional Notes": re.search(r"Additional Notes:\s*(.+)", diagnosis_text),
            "Follow-up": re.search(r"Follow-up:\s*(.+)", diagnosis_text),
        }

        for key, match in sections.items():
            sections[key] = match.group(1).strip() if match else "N/A"

        return sections  

    except requests.exceptions.RequestException as e:
        print("Error in API call:", e)
        return {
            "Diagnosis": "⚠️ AI Diagnosis not available. Please consult a doctor.",
            "Treatment Plan": "N/A",
            "Medicines": "N/A",
            "Additional Notes": "N/A",
            "Follow-up": "N/A",
        }

def diagnose(request):
    if request.method == "POST":
        patient_name = request.POST.get("patient_name", "Unknown Patient").strip()
        age = request.POST.get("age", "N/A").strip()
        gender = request.POST.get("gender", "N/A").strip()
        symptoms = request.POST.get("symptoms", "").strip()
        contact = request.POST.get("contact", "N/A").strip()
        address = request.POST.get("address", "N/A").strip()
        doctor_name = request.POST.get("doctor_name", "Dr. John Doe").strip()
        hospital = request.POST.get("hospital", "Unknown Hospital").strip()
        specialization = request.POST.get("specialization", "General Physician").strip()

        if not symptoms:
            return render(request, "report_form.html", {"error": "Please enter symptoms."})

        diagnosis_data = get_medical_diagnosis(patient_name, age, gender, symptoms)

        context = {
            "patient_name": patient_name,
            "age": age,
            "gender": gender,
            "symptoms": symptoms,
            "contact": contact,
            "address": address,
            "doctor_name": doctor_name,
            "hospital": hospital,
            "specialization": specialization,
            "diagnosis_data": diagnosis_data
        }

        return render(request, "preview_report.html", context)

    return render(request, "report_form.html")



from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

def generate_pdf_report(patient_name, age, gender, symptoms, contact, address, diagnosis_data, doctor_name, specialization, hospital):
    """Creates a polished and structured AI-generated medical report in PDF format."""

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(name="TitleStyle", parent=styles["Title"], alignment=TA_CENTER, fontSize=20, spaceAfter=20)
    section_heading = ParagraphStyle(name="SectionHeading", parent=styles["Heading2"], spaceBefore=12, spaceAfter=6)
    body_text = styles["BodyText"]

    elements = []

    # Title
    elements.append(Paragraph("🩺 Medical Diagnosis Report", title_style))
    elements.append(HRFlowable(width="100%", thickness=1, color="#555555"))
    elements.append(Spacer(1, 12))

    # Patient Details
    patient_info = f"""
    <b>Patient Name:</b> {patient_name}<br/>
    <b>Age:</b> {age}<br/>
    <b>Gender:</b> {gender}<br/>
    <b>Contact:</b> {contact}<br/>
    <b>Address:</b> {address}<br/>
    <b>Symptoms:</b> {symptoms}
    """
    elements.append(Paragraph(patient_info.strip(), body_text))
    elements.append(Spacer(1, 12))

    # Diagnosis Section
    elements.append(Paragraph("Diagnosis", section_heading))
    elements.append(Paragraph(diagnosis_data.get("Diagnosis", "N/A"), body_text))
    elements.append(Spacer(1, 10))

    # Treatment Plan
    elements.append(Paragraph("Treatment Plan", section_heading))
    elements.append(Paragraph(diagnosis_data.get("Treatment Plan", "N/A"), body_text))
    elements.append(Spacer(1, 10))

    # Recommended Medicines
    elements.append(Paragraph("Recommended Medicines", section_heading))
    elements.append(Paragraph(diagnosis_data.get("Medicines", "N/A"), body_text))
    elements.append(Spacer(1, 10))

    # Additional Notes
    elements.append(Paragraph("Additional Notes", section_heading))
    elements.append(Paragraph(diagnosis_data.get("Additional Notes", "N/A"), body_text))
    elements.append(Spacer(1, 10))

    # Follow-up
    elements.append(Paragraph("Follow-up", section_heading))
    elements.append(Paragraph(diagnosis_data.get("Follow-up", "N/A"), body_text))
    elements.append(Spacer(1, 16))

    # Doctor Info
    doctor_info = f"""
    <b>Doctor:</b> {doctor_name} ({specialization})<br/>
    <b>Hospital:</b> {hospital}
    """
    elements.append(Paragraph(doctor_info.strip(), body_text))
    elements.append(Spacer(1, 20))

    # Disclaimer
    elements.append(HRFlowable(width="100%", thickness=1, color="#888888"))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph("⚠️ AI Disclaimer", section_heading))
    elements.append(Paragraph(
        "This medical report was generated using AI and is intended for informational purposes only. "
        "It should not replace consultation with a licensed healthcare professional.",
        body_text
    ))

    doc.build(elements)
    buffer.seek(0)
    return buffer


def analyze_medical_image(image_path):
    """Sends an X-ray or CT scan image to OpenRouter and gets a diagnosis."""
    
    # Convert image to base64 format
    with open(image_path, "rb") as img_file:
        base64_image = base64.b64encode(img_file.read()).decode("utf-8")

    prompt = """
    You are an AI medical assistant. Analyze the given X-ray or CT scan image 
    and provide:
    1. Possible diagnosis (disease detected).
    2. Recommended medications.
    3. Additional medical advice.
    """

    payload = {
        "model": "google/gemma-3-1b-it:free",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": [{"type": "image", "image": base64_image}]}
        ]
    }
   
    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        data = response.json()

        # Extract response
        diagnosis_text = data.get("choices", [{}])[0].get("message", {}).get("content", "Diagnosis not available.")

        return diagnosis_text

    except requests.exceptions.RequestException as e:
        print("Error in API call:", e)
        return "⚠️ AI Diagnosis not available."

def image_diagnosis(request):
    diagnosis_result = None
    image_url = None

    if request.method == "POST":
        form = MedicalImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data["image"]
            
            # Define upload path
            upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
            os.makedirs(upload_dir, exist_ok=True)  # Ensure directory exists

            image_path = os.path.join(upload_dir, image.name)

            # Save the uploaded image
            with open(image_path, "wb") as f:
                for chunk in image.chunks():
                    f.write(chunk)

            image_url = settings.MEDIA_URL + 'uploads/' + image.name  # Generate URL for display

            # Analyze the image
            diagnosis_result = analyze_medical_image(image_path)

    else:
        form = MedicalImageForm()

    return render(request, "image_diagnosis.html", {"form": form, "diagnosis_result": diagnosis_result, "image_url": image_url})



def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    return text

def analyze_lab_report(report_path):
    # Check file type
    if report_path.endswith(".pdf"):
        report_text = extract_text_from_pdf(report_path)
    else:
        with open(report_path, "rb") as img_file:
            base64_image = base64.b64encode(img_file.read()).decode("utf-8")
        report_text = f"[Image of lab report: {base64_image}]"

    prompt = f"""
    You are an AI medical assistant. Analyze the given lab report and provide:
    1. A summary of the test results.
    2. Possible medical insights.
    3. Any abnormal findings with explanations.
    4. Suggested next steps.
    
    Lab Report:
    {report_text}
    """

    headers = {"Authorization": f"Bearer {settings.OPENROUTER_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "google/gemma-3-1b-it:free",
        "messages": [{"role": "system", "content": prompt}]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"⚠️ Error processing report: {e}"

def lab_report_analysis(request):
    report_result = None
    if request.method == "POST":
        form = LabReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.cleaned_data["report"]
            report_path = f"media/uploads/{report.name}"
            with open(report_path, "wb") as f:
                for chunk in report.chunks():
                    f.write(chunk)

            # Analyze the lab report
            report_result = analyze_lab_report(report_path)
    else:
        form = LabReportForm()

    return render(request, "lab_report_analysis.html", {"form": form, "report_result": report_result})
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse

def forgot_password_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        user = User.objects.filter(email=email).first()
        
        if user:
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = request.build_absolute_uri(reverse('reset_password', args=[uid, token]))
            
            send_mail(
                "Password Reset Request",
                f"Click the link to reset your password: {reset_url}",
                "noreply@yourdomain.com",
                [email],
                fail_silently=False,
            )
            messages.success(request, "Password reset link sent to your email.")
        else:
            messages.error(request, "Email not found. Please check and try again.")

    return render(request, "forgot_password.html")
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()

def reset_password_view(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        if request.method == "POST":
            new_password = request.POST.get("password")
            user.password = make_password(new_password)
            user.save()
            messages.success(request, "Password reset successful. You can now login.")
            return redirect("login")
        return render(request, "reset_password.html")
    else:
        messages.error(request, "Invalid or expired reset link.")
        return redirect("forgot_password")
