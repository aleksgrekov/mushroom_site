from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edible/', views.edible_mushrooms, name='edible_mushrooms'),
    path('poisonous/', views.poisonous_mushrooms, name='poisonous_mushrooms'),
    path('gallery/', views.gallery, name='gallery'),
    path('identifier/', views.interactive_identifier, name='interactive_identifier'),
    path('mushroom/<int:mushroom_id>/', views.mushroom_detail, name='mushroom_detail'),
    path('quiz/', views.quiz_home, name='quiz_home'),
    path('quiz/<int:quiz_id>/start/', views.quiz_start, name='quiz_start'),
    path('quiz/question/', views.quiz_question, name='quiz_question'),
    path('quiz/check-answer/', views.quiz_check_answer, name='quiz_check_answer'),
    path('quiz/result/', views.quiz_result, name='quiz_result'),
    path('kingdom/', views.kingdom_info, name='kingdom_info'),
    path('quiz/export/', views.export_quiz_results, name='export_quiz_results'),
    path('quiz/results/<int:result_id>/', views.quiz_results_detail, name='quiz_results_detail'),
]