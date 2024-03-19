from django.urls import path
from emailsender import views

urlpatterns = [
    path('', views.send_mail, name="contact")
]