from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_textbook, name='all_textbooks'),  # root
    path('textbooks/', views.add_textbook_any, name='add_textbook_any'),
    path('textbooks/<str:course_code>/', views.course_textbook, name='course_textbooks'),
]
