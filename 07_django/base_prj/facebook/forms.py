from django import forms
from .models import Newsfeed, Comment


class NewsfeedModelForm(forms.ModelForm):
    class Meta:
        model = Newsfeed
        fields = "__all__"


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
