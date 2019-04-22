from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .forms import CustomUserAuthenticationForm, CustomUserCreateForm
from .models import User
# 또는 from django.contrib.auth import get_user_model()
from posts.forms import CommentModelForm
from IPython import embed


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreateForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("insta:post_list")
    else:
        form = CustomUserCreateForm()
    return render(request, "accounts/signup.html", {"form": form})


@require_http_methods(["GET", "POST"])
def login(request):
    if request.user.is_authenticated: # 로그인이 되어 있다면
        return redirect("insta:post_list")
    if request.method == "POST": # 사용자가 이미 로그인 데이터를 넘겼을때
        form = CustomUserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "insta:post_list")
    else: # 사용자가 로그인 화면을 요청할 때
        form = CustomUserAuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


def logout(request):
    auth_logout(request)
    messages.add_message(request, messages.SUCCESS, "로그아웃 되었습니다.")
    return redirect("insta:post_list")


def user_detail(request, username):
    user_info = User.objects.get(username=username)
    return render(request, "accounts/user_detail.html", {
        "user_info": user_info,
        "comment_form" : CommentModelForm,
    })


@login_required()
@require_POST
def follow_user(request, username):
    post_user = User.objects.get(username=username)
    if request.user != post_user:
        if request.user in post_user.follow.all():
            post_user.follow.remove(request.user)
        else:
            post_user.follow.add(request.user)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/insta/"))
