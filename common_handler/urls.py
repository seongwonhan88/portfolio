from django.urls import path

from .views import get_covid19_states, health_check

urlpatterns = [
    path('covid_19/<str:group>/', get_covid19_states),
    path('health_check/', health_check),
]
