from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer
from users.models import CustomUser


# Create your views here.

@api_view(["GET"])
@permission_classes([IsAuthenticatedOrReadOnly])
def getList(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getListByUserId(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
        if request.user != user:
            return Response({"message": "You do not have permission!"}, status=403)
        notes = Note.objects.filter(user=user)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    except CustomUser.DoesNotExist:
        return Response({"message": "User not found."}, status=404)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create(request, user_id):
    note_data = request.data
    try:
        user = CustomUser.objects.get(id=user_id)
        if request.user != user:
            return Response({"message": "You do not have permission!"}, status=403)
    except CustomUser.DoesNotExist:
        return Response({"message": "User not found."}, status=404)

    serializer = NoteSerializer(data=note_data)
    if serializer.is_valid():
        serializer.save(user=user)
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update(request, user_id ,note_id):
    try:
        user = CustomUser.objects.get(id=user_id)
        if request.user != user:
            return Response({"message": "You do not have permission!"}, status=403)
    except CustomUser.DoesNotExist:
        return Response({"message": "User not found."}, status=404)
    note = Note.objects.get(id = note_id)
    serializer = NoteSerializer(instance=note,data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete(request, user_id,note_id):
    try:
        user = CustomUser.objects.get(id=user_id)
        if request.user != user:
            return Response({"message": "You do not have permission!"}, status=403) 
    except CustomUser.DoesNotExist:
        return Response({"message": "User not found."}, status=404)
    note = Note.objects.get(id = note_id)
    note.delete()
    return Response("deleted note successfully!")