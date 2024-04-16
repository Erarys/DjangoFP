from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from rx import of
from rx.operators import concat
import rx.operators as op
import logging

data_rx = {}


class ReactiveXListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        global data_rx

        if not data_rx.get("session"):
            source = of("Task_1", "Task_2", "Task_3", "Task_4")
        else:
            source = data_rx["session"]

        next = []
        error = []
        complete = []
        source.subscribe(
            on_next=lambda i: next.append(i),
            on_error=lambda e: error.append(e),
            on_completed=lambda: complete.append("Done"),
        )
        context = {
            "next": next,
            "error": error,
            "source": source
        }
        data_rx = {
            "session": source
        }

        return render(request, 'FPtask/rx-list.html', context)

    def post(self, request: HttpRequest) -> HttpResponse:

        action = request.POST.get("action")
        data = request.POST.get("data")
        if not data_rx.get("session"):
            source = of("Task_1", "Task_2", "Task_3", "Task_4")
        else:
            source = data_rx.get("session")

        if action == "add":
            source = source.pipe(concat(of(data)))
        elif action == "del":
            source = source.pipe(op.filter(lambda i: i != data))

        data_rx["session"] = source
        url = request.path
        return redirect(url)
