from django.contrib import admin
from .models import Student, Lecture, Enrolment

admin.site.register([Student, Lecture, Enrolment])