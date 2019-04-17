from django.db import models
from django_extensions.db.models import TimeStampedModel
from faker import Faker
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User
from django.conf import settings


# import os
# ENV = os.environ.get("ENVIRONMENT", "development")
# if ENV == "development":
#     from faker import Faker
#     from IPython import embed

faker = Faker()


class Post(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)

    @classmethod
    def dummy(cls, N):
        for _ in range(N):
            Post.objects.create(content=faker.text(139))


class Image(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = ProcessedImageField(
        blank=True,
        upload_to="posts/images",
        processors=[ResizeToFill(600, 600, upscale=False)],
        format="JPEG",
        options={"quality": 90}
        )


class Comment(TimeStampedModel):
    content = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)