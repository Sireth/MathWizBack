from django.urls import path
from .views import EvaluationApi

urlpatterns = [
    path('evaluation/', EvaluationApi.as_view(), name='evaluation'),
]