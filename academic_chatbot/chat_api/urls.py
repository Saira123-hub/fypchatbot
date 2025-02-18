from django.urls import path
from .views import academic_chatbot

urlpatterns = [
    path('chat/', academic_chatbot, name="academic_chatbot"),
]