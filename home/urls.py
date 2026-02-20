from django.contrib import admin
from django.urls import path
from healthai import urls
from django.urls import path, include

from django.urls import path
from .views import signup_view, verify_email_view, login_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('verify-email/', verify_email_view, name='verify_email'),
    path('login/', login_view, name='login'),
]
