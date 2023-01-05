from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(label='Student name ', max_length=20)
    