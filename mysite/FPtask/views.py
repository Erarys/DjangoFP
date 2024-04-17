from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
import logging


logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")


class GetAndUpperTextView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        logging.info("GetAndUpperTextView called")
        print("HELLO WORLD")
        return render(request, 'FPtask/get-and-upper-text.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        text = request.POST.get('text')

        if not text:
            logging.critical("user send nothing")
        text = ''.join(text.split()).lower()
        context = {
            "upper_text": text
        }
        return render(request, 'FPtask/get-and-upper-text.html', context)


