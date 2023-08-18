from django.urls import path
from . import views

urlpatterns = [
    path("", views.getList), 
    path("<str:user_id>", views.getListByUserId),
    path("<str:user_id>/create/", views.create),
    path("<str:note_id>/update/<str:user_id>", views.update),
    path("<str:note_id>/delete/<str:user_id>", views.delete),
]
