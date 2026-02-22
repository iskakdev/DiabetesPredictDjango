from django.urls import path
from .views import DiabetesPredict

urlpatterns = [
    path('predict/', DiabetesPredict.as_view(), name='diabetes_predict')
]
