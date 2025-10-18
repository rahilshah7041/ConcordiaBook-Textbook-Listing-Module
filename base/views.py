from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from .models import Course, Textbook
from django.urls import reverse

class TextbookForm(forms.ModelForm):
    class Meta:
        model = Textbook
        fields = ['title', 'author', 'isbn']

def course_textbooks(request, course_code):
    course = get_object_or_404(Course, code=course_code)
    textbooks = course.textbooks.all()

    if request.method == 'POST':
        form = TextbookForm(request.POST)
        if form.is_valid():
            new_textbook = form.save(commit=False)
            new_textbook.course = course
            new_textbook.save()
            return redirect('course_textbooks', course_code=course.code)
    else:
        form = TextbookForm()

    return render(request, 'course_textbooks.html', {
        'course': course,
        'textbooks': textbooks,
        'form': form
    })

def all_textbooks(request):
    textbooks = Textbook.objects.select_related('course').all()
    return render(request, 'all_textbooks.html', {'textbooks': textbooks})