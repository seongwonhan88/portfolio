from django.urls import path

from common_handler.views import get_covid19_states

urlpatterns = [
    path('covid_19/<str:group>/', get_covid19_states),
]
