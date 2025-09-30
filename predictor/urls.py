from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict_form, name='predict_form'),
    path('predict-api/', views.predict_api, name='predict_api'),
]