"""
URL configuration for healthai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from home.views import signup_view, verify_email_view, login_view,resend_otp_view,logout_view

from django.shortcuts import redirect
from django.views.generic import TemplateView
from home.views import forgot_password_view, reset_password_view
urlpatterns = [
 
 
       path('signup/', signup_view, name='signup'),
    path('verify-email/', verify_email_view, name='verify_email'),
    path('login/', login_view, name='login'),
    path('ads.txt/', views.ads, name='ads'),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path("sitemap.xml/", views.sitemap, name="sitemap"),
    path("robots.txt/", views.robots, name="robots"),
#    path("admin/",include('admin.site.urls')),
       path('accounts/', include('home.urls')),
    path('',views.home,name="home"),
        path('verify-email/', verify_email_view, name='verify_email'),
    path('about',views.aboutdisplay,name="aboutdisplay"),
    path("diagnose/", views.diagnose, name="diagnose"),
    path('forgot-password/', forgot_password_view, name='forgot_password'),
    path('reset-password/<uidb64>/<token>/', reset_password_view, name='reset_password'),
   
    path('accounts/', include('home.urls')),
        path('resend-otp/', resend_otp_view, name='resend_otp'),  # ✅ Add this line
         path('logout/', logout_view, name='logout'),
    path("lab-report-analysis/", views.lab_report_analysis, name="lab_report_analysis"),
     path('contact/', views.contact_us, name='contact_us'),
    path("image-diagnosis/", views.image_diagnosis, name="image_diagnosis"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
