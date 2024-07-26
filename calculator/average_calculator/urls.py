from django.urls import path
from .views import avg_calculator

urlpatterns = [
    path('numbers/<str:qualifier>/', avg_calculator),
]
