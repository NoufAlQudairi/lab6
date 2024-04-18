from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from .models import Student,Course

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


# Create your views here.

def students(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)

        if(form.is_valid):
            form.save()
            return HttpResponseRedirect(reverse("school:students"))
        else:
            return render(request, "school/students.html",{
                "message":"invalid data enterd for a student."
            })


    return render(request, "school/students.html", {
        "students" : Student.objects.all(),
        "form" : StudentModelForm()
    })


def courses(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)

        if(form.is_valid):
            form.save()
            return HttpResponseRedirect(reverse("school:courses"))
        else:
            return render(request, "school/courses.html",{
                "message":"invalid data enterd for a course."
            })


    return render(request, "school/courses.html", {
        "courses" : Course.objects.all(),
        "form" : CourseModelForm()
    })

def details(request, student_id):
    
    if request.method == "POST":
        try:
            course = Course.objects.get(pk=int(request.POST["course"]))
            student = Student.objects.get(pk=student_id)
        except KeyError:
            return HttpResponseBadRequest("Bad Request: no Student chosen")
        except Student.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: Student does not exist")
        except Course.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: Course does not exist")
        student.courses.add(course)
        return HttpResponseRedirect(reverse("school:details", args=(student_id,)))
    
    try:
        student = Student.objects.get(pk = student_id)
    except Student.DoesNotExist:
        raise Http404("Student not found.")
    
    return render(request, "school/details.html", {
        "student": student,
        "courses": student.courses.all(),
        "notRegisteredCourses": Course.objects.exclude(students=student).all()
    })

  
