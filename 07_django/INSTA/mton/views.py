from django.shortcuts import render
from .models import Student, Lecture, Enrolment


# Create your views here.

# def mton_index(request):
#     student = Student.objects.get(id=1)
#     enrolments = student.enrolment_set.all()
#     lectures = []
#     for enrol in enrolments:
#         lectures += [enrol.lecture.name]
#
#     return render(request, "mton/index.html", {
#         "lectures": lectures,
#     })
