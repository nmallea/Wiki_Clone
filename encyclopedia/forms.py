from django import forms

class createEntry(forms.Form):
    entryTitle = forms.CharField(label="Create Entry", max_length=100)
    content = forms.CharField(label="Mark Down", widget=forms.Textarea)

class editEntry(forms.Form):
    markDown = forms.CharField(label="Mark Down", widget=forms.Textarea)