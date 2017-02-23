from django.shortcuts import render, redirect
from .models import Course
# Create your views here.


def index(request):
    context = {
        "courses": Course.objects.all(),
    }
    return render(request, "courses/index.html", context)


def create(request):
    if request.method == 'POST':
        Course.objects.create(name=request.POST['name'], description=request.POST['description'])

    return redirect('/')


def confirm(request, id):
    context = {
        'course': Course.objects.get(id=id)
    }
    return render(request, "courses/confirm.html", context)


def destroy(request, id):
    Course.objects.get(id=id).delete()
    return redirect("/")
