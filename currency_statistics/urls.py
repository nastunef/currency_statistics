from django.urls import path
from statistic import views as statistics_views


urlpatterns = [
    path('', statistics_views.index),
]
