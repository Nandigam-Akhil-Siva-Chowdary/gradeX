from django import forms
from .models import StudentRecord

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentRecord
        fields = [
            'name', 'reg_number', 'branch', 'calculation_type', 
            'sgpa', 'sem1_gpa', 'sem2_gpa', 'sem3_gpa', 'cgpa'
        ]
        widgets = {
            'calculation_type': forms.HiddenInput(),
            'sgpa': forms.HiddenInput(),
            'sem1_gpa': forms.HiddenInput(),
            'sem2_gpa': forms.HiddenInput(),
            'sem3_gpa': forms.HiddenInput(),
            'cgpa': forms.HiddenInput(),
        }