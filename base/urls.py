from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_textbooks, name='all_textbooks'),
    path('textbooks/<str:course_code>/', views.course_textbooks, name='course_textbooks'),
]
