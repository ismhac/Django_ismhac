from django.urls import path
from . import views

urlpatterns = [
    path("", views.getList), 
    path("<str:user_id>", views.getById),
    path("create/", views.create),
    path("<str:user_id>/update/", views.update),
    path("<str:user_id>/delete/", views.delete),
]