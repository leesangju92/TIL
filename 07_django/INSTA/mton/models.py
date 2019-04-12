from django.db import models
from faker import Faker

faker = Faker()


class Student(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.id} : {self.name}"


class Client(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        ordering = ("name", )

    @classmethod
    def dummy(cls, N):
        for n in range(N):
            cls.objects.create(name=faker.name())


class Hotel(models.Model):
    name = models.CharField(max_length=40)
    clients = models.ManyToManyField(Client)

    @classmethod
    def dummy(cls, N):
        for n in range(N):
            cls.objects.create(name=faker.company())


class Lecture(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.id} : {self.name}"


class Enrolment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)







