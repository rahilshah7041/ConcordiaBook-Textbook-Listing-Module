from django import forms
from .models import Textbook

class TextbookForm(forms.ModelForm):
    class Meta:
        model = Textbook
        fields = ['title', 'author', 'editon', 'course_code']
