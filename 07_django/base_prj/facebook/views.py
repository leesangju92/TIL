from django.shortcuts import render, redirect, get_object_or_404
from .models import Newsfeed, Comment
from .forms import NewsfeedModelForm, CommentModelForm


def index(request):
    newsfeeds = Newsfeed.objects.all()
    return render(request, "facebook/index.html", {"newsfeeds":newsfeeds})


def detail(request, Newsfeed_id):
    newsfeed = get_object_or_404(Newsfeed, id=Newsfeed_id)
    comments = newsfeed.comment_set.all()
    return render(request, "facebook/detail.html", {"newsfeed": newsfeed, "comments": comments})


def create(request):
    if request.method == "POST":
        form = NewsfeedModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("facebook:index")
    else:
        form = NewsfeedModelForm()
    return render(request, "facebook/create.html", {"form": form})
