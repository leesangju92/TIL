from django import forms
from .models import Movie

# class MovieForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     title_en = forms.CharField(max_length=100)
#     audience = forms.IntegerField()
#     open_date = forms.DateField(
#         widget=forms.widgets.DateInput(attrs={"type":"date"})
#     )
#     genre = forms.CharField(max_length=100)
#     watch_grade = forms.CharField(max_length=100)
#     score = forms.FloatField()
#     poster_url = forms.CharField()
#     description = forms.CharField(widget=forms.Textarea())

# input tag 대신 만들어주는 역할


class MovieModelForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"      #리스트 형식으로 지정해줄수 있다.
        widgets = {
            "open_date": forms.DateInput(attrs={"type": "date"})
        }

