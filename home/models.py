from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone


class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE,default="user")
    age = models.IntegerField(default="user")
    gender = models.CharField(max_length=10,default="user")
    diagnosed_disease = models.CharField(max_length=100, blank=True, null=True,default="user")



    def __str__(self):
        return self.user.username


class DiagnosisResult(models.Model):
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    diagnosed_condition = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.user_profile:
            return f"{self.user_profile.username} - {self.diagnosed_condition}"
        return f"Anonymous - {self.diagnosed_condition}"


class DailyPlan(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.user_profile.user.username}'s Plan - {self.date}"
    




from datetime import timedelta

class EmailOTP(models.Model):
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_otp(self):
        import random
        self.otp = str(random.randint(100000, 999999))
        self.created_at = timezone.now()  # update creation time
        self.save()

    def is_otp_expired(self):
        expiration_time = self.created_at + timedelta(minutes=10)
        return timezone.now() > expiration_time
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
# models.py
