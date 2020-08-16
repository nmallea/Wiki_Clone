from django.shortcuts import redirect, render
from markdown2 import Markdown

from . import forms
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

