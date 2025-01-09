from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.main, name='main'),
    path('resume/', views.resume, name='resume'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]
