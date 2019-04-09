from django.shortcuts import render
from .models import Posting, Comment

# Create your views here.


def myway_list(request):
    postings = Posting.objects.all()
    return render(request, "myway/list.html", {"postings": postings})


def myway_detail(request, id):
    posting = Posting.objects.get(id=id)
    return render(request, "myway/detail.html", {"posting": posting})
