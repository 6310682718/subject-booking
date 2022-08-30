from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path('subject/<int:id>', views.subject_id, name="subject_id"),
    # path("subject/<int:id>/book", views.booking_subject, name="booking"),
    # path("student/<index:id>", views.student_subject_list,
    #      name="student_subject_list"),
    # path("student/<index:id>/<int:subject_id>/unbook",
    #      views.unbook_subject, name="unbook_subject")
]
