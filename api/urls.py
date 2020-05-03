from django.urls import path

from api.views.teachers import TeacherAPIView
from api.views.students import StudentAPIView,StudentDetailView
from api.views.courses import SectionAPIView


urlpatterns = [
    path('teachers/', TeacherAPIView.as_view()),
    path('students/', StudentAPIView.as_view()),
    path('students/<code>', StudentDetailView.as_view()),
    path('sections/', SectionAPIView.as_view()),
]
