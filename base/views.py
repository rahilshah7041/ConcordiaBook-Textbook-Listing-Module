from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Textbook
from .forms import TextbookForm, TextbookAnyCourseForm
from django.urls import reverse

def all_textbook(request):
    """
    Root page: show all textbooks (only those available=True).
    Also show list of courses with links to the course-specific add/list page.
    """
    textbooks = Textbook.objects.select_related('course').filter(available=True).order_by('-created_at')
    courses = Course.objects.order_by('code')
    return render(request, 'all_textbooks.html', {
        'textbooks': textbooks,
        'courses': courses,
    })

def course_textbook(request, course_code):
    """
    Course-specific page: show textbooks for course (available=True) and provide form to add a textbook
    for this course.
    """
    course = get_object_or_404(Course, code=course_code)
    textbooks = course.textbooks.filter(available=True).order_by('-created_at')

    if request.method == 'POST':
        form = TextbookForm(request.POST)
        if form.is_valid():
            tb = form.save(commit=False)
            tb.course = course
            tb.save()
            return redirect('course_textbooks', course_code=course.code)
    else:
        form = TextbookForm()

    return render(request, 'course_textbooks.html', {
        'course': course,
        'textbooks': textbooks,
        'form': form,
    })
    
def add_textbook_any(request):
    """
    Page to add a textbook for ANY course.
    If course doesn't exist, it is automatically created.
    """
    if request.method == 'POST':
        form = TextbookAnyCourseForm(request.POST)
        if form.is_valid():
            course_code = form.cleaned_data['course_code'].upper().strip()
            course_name = form.cleaned_data.get('course_name', '').strip() or course_code

            # Create course if it doesn't exist
            course, created = Course.objects.get_or_create(
                code=course_code,
                defaults={'name': course_name}
            )

            # Create textbook linked to this course
            textbook = Textbook(
                course=course,
                title=form.cleaned_data['title'],
                author=form.cleaned_data['author'],
                edition=form.cleaned_data['edition'],
                year=form.cleaned_data['year'],
                condition=form.cleaned_data['condition'],
                available=form.cleaned_data['available']
            )
            textbook.save()

            # Redirect to the course's textbooks page
            return redirect('course_textbooks', course_code=course.code)
    else:
        form = TextbookAnyCourseForm()

    return render(request, 'add_textbook_any.html', {'form': form})