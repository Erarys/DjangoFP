from django.urls import path
from .views import GetAndUpperTextView

app_name = "fp"

urlpatterns = [
    path('', GetAndUpperTextView.as_view(), name="get_and_upper")
]