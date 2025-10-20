from django.db import models

CONDITION_CHOICES = [
    ('new', 'New'),
    ('like_new', 'Like New'),
    ('used', 'Used'),
    ('worn', 'Worn'),
    ('other', 'Other'),
]

class Course(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.code} - {self.name}"

class Textbook(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='textbooks')
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=200)
    edition = models.CharField(max_length=50, blank=True)   # edition optional
    year = models.PositiveIntegerField(null=True, blank=True)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='used')
    available = models.BooleanField(default=True)  # availability flag

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.course.code})"
