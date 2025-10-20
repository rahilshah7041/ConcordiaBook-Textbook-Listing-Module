from django import forms
from .models import Textbook, CONDITION_CHOICES, Course

class TextbookForm(forms.ModelForm):
    class Meta:
        model = Textbook
        fields = ['title', 'author', 'edition', 'year', 'condition', 'available']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Textbook title', 'class': 'input'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author(s)', 'class': 'input'}),
            'edition': forms.TextInput(attrs={'placeholder': 'e.g. 3rd', 'class': 'input'}),
            'year': forms.NumberInput(attrs={'placeholder': 'Year (optional)', 'class': 'input'}),
            'condition': forms.Select(attrs={'class': 'input'}),
            'available': forms.CheckboxInput(),
        }
        labels = {
            'available': 'Available for trade',
        }
        
class TextbookAnyCourseForm(forms.ModelForm):
    course_code = forms.CharField(
        max_length=20,
        label='Course Code',
        help_text='Enter the course code (e.g., COEN6311)'
    )
    course_name = forms.CharField(
        max_length=200,
        label='Course Name',
        required=False,
        help_text='Enter course name (optional, only used if new course)'
    )

    class Meta:
        model = Textbook
        fields = ['course_code', 'course_name', 'title', 'author', 'edition', 'year', 'condition', 'available']