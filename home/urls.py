from django.contrib import admin
from django.urls import path,include
from healthmental import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("healthmental.urls"))
]
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('ybocs_input/', views.ybocs_input, name='ybocs_input'),
      path('gad7/', views.gad7_view, name='gad7_test'),
    path('results/', views.diagnosis_results, name='results'),
    path('daily-plan/', views.daily_plan, name='daily_plan'),
         path('ocd/', views.ocd_detail, name='ocd_detail'),
          path('phq9/', views.phq9_view, name='phq9_test'),
          path('mdq/', views.mdq_view, name='mdq_view'),
         path('anxiety/', views.anxiety, name='anxiety'),
           
         path('bipolar/',views.bipolar,name="bipolar"),
         path("pcl5/",views.pcl5_view,name="pcl5_view"),
                  path('dep/', views.dep, name='dep'),
                  path('ptsd',views.ptsd,name="ptsd"),
                  path('asrs/',views.asrs_view,name="asrs_view"),
                  path('aq/',views.aq_test_view,name="aq_test_view"),
                  path('sssc/',views.schizophrenia_test_view,name="schizophrenia_test_view"),
        path('', views.base_generic, name='base_generic'),
        path('sleeptest/',views.sleep_test_view,name="sleep_test_view"),
        path('pdss/',views.panic_test_view,name="panic_test_view"),
         path('signup/', views.signup_view, name='signup'),
    # Signup page
      # OTP verification page
    path('resend-otp/', views.resend_otp, name='resend_otp'),  # Resend OTP page
    path('login/', views.login_view, name='login'),  # assuming login_view exists
     
    path('verify-otp/', views.verify_otp, name='verify_otp'),
      path('contact/', views.contact_view, name='contact'),
    path('', views.home, name='home'),  # home page after login
]
