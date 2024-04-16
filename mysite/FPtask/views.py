from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View


class GetAndUpperTextView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'FPtask/get-and-upper-text.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        text = request.POST.get('text')
        text = ''.join(text.split()).lower()
        context = {
            "upper_text": text
        }
        return render(request, 'FPtask/get-and-upper-text.html', context)