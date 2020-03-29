from django.urls import path

from common_handler.views import get_covid19_status

urlpatterns = [
    path('covid_19/', get_covid19_status),
]
