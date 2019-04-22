# 유저 모델 확장 가능성을 염두하라는 취지.
# # django-admin startproject My_Project
# # django-admin startapp accounts
# # accounts/models.py => 아래에 있는 코드 작성
# # settings.py ==> INSTALLED APPS => "accounts"
# # setting.py ==> AUTH_USER_MODEL = "accounts.User"

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="follower", blank=True)
    # 여기서 settings.AUTH_USER_MODEL 은 문자열, 진짜 클래스를 불러오려면 get_user_model() 를 써야한다. (import필요)

    def __str__(self):
        return self.username