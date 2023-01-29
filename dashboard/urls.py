from django.urls import path
from .mako_base_test import Base

urlpatterns = [
    path('base/', Base.as_view()),
]
