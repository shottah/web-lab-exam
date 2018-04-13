from django.shortcuts import render, redirect
from .courses import Course
from .form import CourseForm
from .courses import CourseSerializer
from rest_framework import viewsets
# Create your views here.
def index (request):
    all_courses = Course.objects.all()
    return render(request, 'course/table.html', {'courses': all_courses})

def create_course (request):
    form = CourseForm()

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CourseForm()
    
    return render(request, 'course/add.html', {'form':form})

class CourseViewSet (viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer