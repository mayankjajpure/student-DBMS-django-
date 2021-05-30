from django import forms
from stu_records.models import students

class strecord(forms.ModelForm):
    class Meta:
        model=students
        fields="__all__"

