from django.shortcuts import render

def staticfiles(request):
    return render(request,'staticfiles.html')