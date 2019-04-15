from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Writer(TimeStamp):
    name = models.CharField(max_length=100)


class Book(TimeStamp):
    author = models.ForeignKey(Writer, on_delete=models.PROTECT)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()


class MagazineArticle(TitleDescriptionModel, TimeStampedModel):
    content = models.TextField()


class Chapter(TitleDescriptionModel, TimeStampedModel):
    # title, description, created, modified 기본 제공
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
