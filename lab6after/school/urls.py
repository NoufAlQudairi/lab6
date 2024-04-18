from django.urls import path

from . import views

app_name='school'

urlpatterns = [
    path("", views.students, name="students"),
    path("courses", views.courses, name="courses"),
    path("<int:student_id>", views.details, name="details"),
    
]
