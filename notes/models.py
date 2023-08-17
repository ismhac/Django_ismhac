from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
        db_table = "tbl_notes"
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self) -> str:
        return self.title
