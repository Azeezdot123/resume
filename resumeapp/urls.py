from django.urls import path
from resumeapp import views

urlpatterns = [
    path('', views.contact, name='contact'),
]
