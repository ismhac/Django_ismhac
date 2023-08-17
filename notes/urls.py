from django.urls import path
from . import views

urlpatterns = [
    path("", views.getListByUserId), 
    path("<str:note_id>", views.getById),
    path("create/", views.create),
    path("<str:note_id>/update/", views.update),
    path("<str:note_id>/delete/", views.delete),
]
