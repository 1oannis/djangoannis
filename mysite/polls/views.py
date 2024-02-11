"""Polls views"""

from django.http import HttpResponse


def index(request):
    """Polls view"""
    return HttpResponse("Hello, world. You're at the polls index.")
