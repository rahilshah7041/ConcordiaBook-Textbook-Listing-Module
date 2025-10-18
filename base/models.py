from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.code

class Textbook(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='textbooks', null=True, blank=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.title
