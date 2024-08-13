from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('selectSubj/', views.selectSubj, name='selectSubj'),
    path('examPage/<int:exam_id>/', views.examPage, name='examPage'),
    path('exam_completed/<int:exam_id>/', views.exam_completed, name='exam_completed'),
    # path('debug_exam_results/<int:exam_id>/', views.debug_exam_results, name='debug_exam_results'),

]
