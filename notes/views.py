from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer


# Create your views here.

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getListByUserId(request):
    user = request.user
    notes = Note.objects.filter(user=user)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getById(request, note_id):
    user = request.user
    note = Note.objects.filter(user=user).get(id=note_id)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create(request):
    note = request.data
    serializer = NoteSerializer(data=note)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update(request, note_id):
    note = Note.objects.get(id = note_id)
    serializer = NoteSerializer(instance=note,data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete(request, note_id):
    try:
        note = Note.objects.get(id=note_id, user=request.user)
        note.delete()
        return Response({"message": "Note deleted successfully."}, status=204)
    except Note.DoesNotExist:
        return Response({"message": "Note not found."}, status=404)