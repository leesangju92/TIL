from django.shortcuts import render, redirect
from .models import netflix
# Create your views here.


def index(request):
    movies = netflix.objects.all()
    return render(request, "netflix/index.html", {
        "movies": movies,
    })


def detail(request, id):
    movie = netflix.objects.get(id=id)
    return render(request, "netflix/detail.html", {
        "movie": movie,
    })


def new(request):
    return render(request, "netflix/new.html")


def create(request):
    movie = netflix()
    movie.title = request.POST.get("input_title")
    movie.content = request.POST.get("input_content")
    movie.save()
    return redirect(f"/netflix/{movie.id}/")


def edit(request, id):
    movie = netflix.objects.get(id=id)
    return render(request, "netflix/edit.html", {
        "movie": movie,
    })


def update(request, id):
    movie = netflix.objects.get(id=id)
    movie.title = request.POST.get("input_title")
    movie.content = request.POST.get("input_content")
    movie.save()
    return redirect(f"/netflix/{movie.id}/")


def delete(request, id):
    movie = netflix.objects.get(id=id)
    movie.delete()
    return redirect("/netflix/")
