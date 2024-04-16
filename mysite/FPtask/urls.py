from django.urls import path
from .views import test

app_name = "fp"

urlpatterns = [
    path('', test, name="test")
]