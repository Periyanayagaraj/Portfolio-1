from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'jaga/index.html')


def skills(request):
    return render(request,'jaga/skills.html')


def projects(request):
    return render(request,'jaga/projects.html')


def about(request):
    return render(request,'jaga/about.html')


def hireme(request):
    return render(request,'jaga/hireme.html')