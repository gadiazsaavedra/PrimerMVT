# sourcery skip: docstrings-for-modules
from django.http import HttpResponse


def index(request) -> HttpResponse:
    return HttpResponse("<a href=familia/>Link a familiares</a>")
