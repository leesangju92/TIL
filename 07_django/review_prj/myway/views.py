from django.shortcuts import render, redirect, get_object_or_404
from .models import Posting, Comment
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed
from django.views.decorators.http import require_http_methods


@require_http_methods("GET")
def myway_list(request):
    postings = Posting.objects.all()
    return render(request, "myway/list.html", {"postings": postings})


def myway_detail(request, id):
    posting = get_object_or_404(Posting, id=id)
    comments = posting.comment_set.all()
    return render(request, "myway/detail.html", {"posting": posting, "comments": comments})


def myway_new(request):
    if request.method == "POST":
        P = Posting()
        P.title = request.POST.get("title")
        P.content = request.POST.get("content")
        P.save()
        return redirect("myway:myway_detail", id=P.id)
    else:
        return render(request, "myway/new.html")


@require_http_methods(["POST", "GET"])
def myway_edit(request, id):
    P = get_object_or_404(Posting, id=id)
    if request.method == "POST":
        P.title = request.POST.get("title")
        P.content = request.POST.get("content")
        P.save()
        return redirect("myway:myway_detail", id=P.id)
    else:
        return render(request, "myway/edit.html", {
            "posting": P,
        })


@require_http_methods("POST")
def myway_delete(request, id):
    P = get_object_or_404(Posting, id=id)
    P.delete()
    return redirect("myway:myway_list")


@require_http_methods("POST")
def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, posting_id) #이렇게 확인하는 과정을 꼭 거치도록 하자.
    comment = Comment()
    comment.posting_id = posting.id
    comment.content = request.POST.get("content")
    comment.save()
    return redirect("myway:myway_detail", id=posting.id)


@require_http_methods("POST")
def delete_comment(request, posting_id, comment_id):
    posting = get_object_or_404(Posting, id=posting_id) #사용자를 가능한 믿지 말기
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect("myway:myway_detail", id=posting.id)