from django.shortcuts import render


def homePage(request):
    return render(request, "home.html")


def workPage(request):
    return render(request, "work.html")


def projectPage(request):
    return render(request, "Project.html")
