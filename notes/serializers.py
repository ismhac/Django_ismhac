from rest_framework import serializers
from .models import Note
from users.models import CustomUser


class NoteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), required=False)
    class Meta:
        model = Note
        fields = "__all__"
