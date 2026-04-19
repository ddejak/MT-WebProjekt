from django.urls import path
from . import views

app_name = 'studenti'

urlpatterns = [
    path('', views.index, name='index'),
    path('student/<int:student_id>/', views.student_detail, name='detail'),
]
