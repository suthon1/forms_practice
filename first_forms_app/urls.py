from django.urls import path
from .views import index, add_student_function

urlpatterns = [
    path('main-page/', index, name='index'),
    path('add-student/', add_student_function, name='add-student'),
]