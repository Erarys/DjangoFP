from django.urls import path
from .views import ReactiveXListView

app_name = "fp"

urlpatterns = [
    path('rx/', ReactiveXListView.as_view(), name="test")
]