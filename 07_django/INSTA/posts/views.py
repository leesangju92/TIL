from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Post, Image
from .forms import PostModelForm, ImageModelForm, CommentModelForm
from django.contrib.auth.decorators import login_required
from django.forms import HiddenInput


@login_required()
@require_http_methods(['GET', 'POST'])
def create_post(request):
    # POST 방식으로 넘온 Data 를 ModelForm 에 넣는다.
    if request.method == 'POST':
        # POST 방식으로 넘온 Data 를 ModelForm 에 넣는다.
        post_form = PostModelForm(request.POST)
        # Data 검증을 한다.
        if post_form.is_valid():
            # 통과하면 저장한다.
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            for image in request.FILES.getlist("file"):
                request.FILES["file"] = image  # 딕셔너리 자료형으로 추측된다.
                image_form = ImageModelForm(files=request.FILES)
                if image_form.is_valid():
                    # image = Image()
                    # image.file = request.FILES.get("image")
                    image = image_form.save(commit=False)
                    image.post = post
                    image.save()

            return redirect('insta:post_list')
        # else:
        #     # 실패하면, 다시 data 입력 form 을 준다.
        #     pass
    # GET 방식으로 요청이 오면,
    else:
        # 새로운 Post용 form을 만든다.
        post_form = PostModelForm()
    image_form = ImageModelForm()
    # 사용자에게 form을 넘긴다.
    return render(request, 'posts/form.html', {
        'post_form': post_form,
        "image_form": image_form,
    })


# @login_required()
@require_GET
def post_list(request):
    posts = Post.objects.all()
    comment_form = CommentModelForm()
    return render(request, 'posts/list.html', {'posts': posts, "comment_form":comment_form, })


@login_required()
@require_http_methods(["GET", "POST"])
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.user == request.user:  # 지금 수정하려는 요청 보낸 사람이 작성자인지 확인
        if request.method == "POST":
            post_form = PostModelForm(request.POST, request.FILES, instance=post)
            if post_form.is_valid():
                post_form.save()
                return redirect("insta:post_list")
        else:
            post_form = PostModelForm(instance=post)
        return render(request, "posts/form.html", {"post_form": post_form, })
    else:  # 작성자와 요청 보낸 유저가 다를 경우
        # 에러코드 403 : forbidden
        return redirect("insta:post_list")


def post_detail(request, post_id):
    pass


@login_required()
@require_http_methods(["POST"])
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        comment_form = CommentModelForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect("insta:post_list")
        # TODO: else => comment가 유효하지 않다면 어떻게 해야하지?
