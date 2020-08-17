from django.shortcuts import redirect, render
from markdown2 import markdown
from django.http import HttpResponseRedirect
from . import forms
from . import util


# Create your views here.

#entry page, index, search, create new entry, edit entry, random, convert markdown

def entry(request, title):
    content = util.get_entry(title)
    if not content:
        return render(request, "encyclopedia/error.html", {
            "message": "\"" + title + "\" is not an entry. Feel free to add to Wiki."
        })
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": markdown(content)
    })

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    search_request = request.GET.get("q")
    content = util.get_entry(search_request)
    if not content:
        result = []
        for title in util.list_entries():
            if search_request.casefold() in title.casefold():
                result.append(title)
        return render(request, "encyclopedia/search.html", {
            "result": result
        })
    return render(request, "encyclopedia/entry.html", {
        "title": search_request,
        "content": markdown(content)
    })

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        for entry in util.list_entries():
            if title.casefold() == entry.casefold():
                return render(request, "encyclopedia/create.html", {
                    "message": "",
                    "title": title,
                    "content": content
                })
        util.save_entry(title, content)
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries(),
            "message": "Your entry has been added to the Encyclopedia. Thank you for contributing!"
        })
    return render(request, "encyclopedia/create_entry.html")

def edit(request, title):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        util.save_entry(title, content)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": markdown(content),
            "message": "\"" + title + "\" has been edited and saved."
        })
    content = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content
    })

# def random_entry(request):


