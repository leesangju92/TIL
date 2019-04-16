from django.shortcuts import render, redirect
from .forms import *
from .models import Writer, Book, Chapter


# # create
# def create(request):
#
#     if request.method == "POST":
#         form = WriterModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("detail")
#         else:
#             pass
#     elif request.method == "GET":
#         form = WriterModelForm() # 이걸 앞으로 당겨야함. 만약 valid 검사를 통과하지못한 경우 새 form을 제공하고 싶다면.
#     return render(request, "new.html", {
#             "form": form}
#             )
#
#
# # update
# def update(request, id):
#     writer = Writer.objects.get(id=id)
#     form = WriterModelForm(request.POST, instance=writer)
#     if request.method == "GET":
#         return render(request, "update.html", {
#             "form": form,
#         })
#     else:
#         form = WriterModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("성공!")
#         else:
#             return redirect("실패!")
