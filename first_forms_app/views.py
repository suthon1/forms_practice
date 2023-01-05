from django.shortcuts import render
from .froms import StudentForm
from django.http import HttpResponse
from .models import Student

def index(request):
    return render(request, 'basic.html')


def add_student_function(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student_name = form.cleaned_data['name']
            student = Student.objects.create(name=student_name)
            student.save()
            return HttpResponse('Student name wass added' +  student_name)
    form = StudentForm()
    return render(request, 'first_forms_app/forms.html', {'form': form})