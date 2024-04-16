from django.http import HttpRequest
from django.shortcuts import render


def test(request: HttpRequest):
    return render(request, 'FPtask/base.html')
