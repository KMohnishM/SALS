from django.urls import path
from . import views

urlpatterns = [
    path('generate-quiz/', views.generate_quiz, name='generate_quiz'),
    path('analyze-quiz/', views.analyze_quiz, name='analyze_quiz'),
    path('learning-path/', views.learning_path, name='learning_path'),
    path('final-quiz/', views.final_quiz, name='final_quiz'),
]
