from django.shortcuts import render

from LmsApp import forms
# Create your views here.
from django.http import HttpResponseRedirect

def thanks(request):
    return render(request, 'myApp/thanks.html')

def LibraryView(request):
    if request.method == 'POST':
        form = forms.LibraryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/thanks')
    else:
        form = forms.LibraryForm()
    return render(request, 'myApp/librarydata.html', {'form': form})

