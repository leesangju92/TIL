from django.db import models
from faker import Faker

faker = Faker()


class Song(models.Model):
    name = models.CharField(max_length=200)

    @classmethod
    def dummy(cls, n):
        for _ in range(n):
            cls.objects.create(
                name=faker.catch_phrase()
            )
