from django.shortcuts import render

def screen_viewer(request):
    return render(request, 'displays/viewer.html')
