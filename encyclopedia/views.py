from django.shortcuts import render
from django import forms
from markdown2 import markdown
# from django.http import HttpResponseRedirect
from . import util


# Create your views here.
# class createEntryForm(forms.Form):
#     title = forms.CharField()

#     textarea = forms.CharField(widget=forms.Textarea(attrs={'cols': 80,'rows':10}))
#entry page, index, search, create new entry, edit entry, random, convert markdown

def entry_page(request, title):
    content = util.get_entry(title)
    if not content:
        return render(request, "encyclopedia/error.html", {
            "message": "\"" + title + "\" is not found. Feel free to add to Wiki."
        })
    return render(request, "encyclopedia/entry_page.html", {
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
    return render(request, "encyclopedia/entry_page.html", {
        "title": search_request,
        "content": markdown(content)
    })

def create_entry(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        for entry in util.list_entries():
            if title.casefold() == entry.casefold():
                return render(request, "encyclopedia/create_entry.html", {
                    "message": "encyclopedia entry with same title exists already.",
                    "title": title,
                    "content": content
                })
        util.save_entry(title, content)
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries(),
            "message": "New encyclopedia page added with success!"
        })
    return render(request, "encyclopedia/create_entry.html")


def edit_entry(request, title):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        util.save_entry(title, content)
        return render(request, "encyclopedia/entry_page.html", {
            "title": title,
            "content": markdown(content),
            "message": "\"" + title + "\" has been edited and saved."
        })
    content = util.get_entry(title)
    return render(request, "encyclopedia/edit_entry.html", {
        "title": title,
        "content": content
    })

# def random_entry(request):
