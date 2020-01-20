from django.shortcuts import render

def index(request):
    return render (request, 'services/services.html')

def Coils(request):
    return render (request, 'services/HR MS Coils.html')

def Plates(request):
    return render (request, 'services/HR MS Plates.html')

def Slabs(request):
    return render (request, 'services/MS Slabs.html')

# def pipe(request):
#     return render (request, 'services/pipe.html')

# def tanks(request):
#     return render (request, 'services/tanks.html')

# def stacks(request):
#     return render (request, 'services/stacks.html')