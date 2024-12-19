from django.shortcuts import render

def gs(request):
    return render(request, "base.html")
