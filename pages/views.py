from django.shortcuts import render
from django.http import HttpResponse
from .forms import contact_us,SnippetForm

def index(request):
    return render (request, 'pages/index.html')

def about(request):
    return render (request, 'pages/about.html')

def contact(request):
    if request.method == 'POST':
        form = contact_us(request.POST)
        if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
    
    form = contact_us
    return render (request, 'form.html', {'form': form})

def snippet_details(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
                print("VALID")
    
    form = contact_us
    return render (request, 'form.html', {'form': form})