from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:subject_id>', views.subject_id, name="subject_id"),
    path("<index:subject_id>/book", views.book, name="book")
]
