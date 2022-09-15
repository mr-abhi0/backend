from api import views
from django.urls import path

urlpatterns = [
    path('students/', views.StudentsList.as_view()),
]
