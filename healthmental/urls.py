"""
URL configuration for healthmental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.views.generic import TemplateView

from django.urls import path,include
from home import views
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',include("home.urls")),
      path('ocd/', views.ocd_detail, name='ocd_detail'),
         path('gad7/', views.gad7, name='gad7'),
        path("sitemap.xml", TemplateView.as_view(template_name="sitemap.xml", content_type="application/xml")),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
             path('anxiety/', views.anxiety, name='anxiety'),
                      path('dep/', views.dep, name='dep'),
                      path('phq9/', views.phq9, name='phq9'),        
                                 path('bipolar/',views.bipolar,name="bipolar"),
                            path('mdq/', views.mdq, name='mdq'),  
                            path('pcl5/',views.pcl5,name="pcl5"),
                            path('asrs/',views.asrs,name="asrs"),
                            path('adhd/',views.adhd,name="adhd"),
                            path('aq/',views.aq,name="aq"),
                            path('autism',views.autism,name="autism"),
                            path('schizophrenia/',views.schizophrenia,name="schizophrenia"),
                            path('sssc/',views.sssc,name="sssc"),
                                 path('ptsd',views.ptsd,name="ptsd"),
                                 path('sleeptest/',views.sleeptest,name="sleeptest"),
                                 path('sleep/',views.sleep,name="sleep"),
          path('ybocs_input/', views.ybocs_input, name='ybocs_input'),
          path('pdss/',views.pdss,name="pdss"),
          path("contact/",views.contact,name="contact"),
          path("about/",views.about,name="about"),
          path('panic',views.panic,name="panic"),
          path("", views.home, name="home"),
           path('verify-otp/', views.verify_otp, name='verify_otp'),  # OTP verification page
    path('resend-otp/', views.resend_otp, name='resend_otp'),  # Resend OTP page
          path("login/",views.login,name="login"),
          path("signup/",views.signup,name="signup"),
            path('Logout', views.logout_view, name='logout'),

          path("forgotpassword/",views.forgotpassword,name="forgotpassword"),
          path("resetpassword/",views.resetpassword,name="resetpassword")
]
