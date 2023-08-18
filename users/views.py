from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer


# Create your views here.

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getList(request):
    users = CustomUser.objects.all()
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getById(request, user_id):
    user = CustomUser.objects.get(id = user_id)
    serializer = CustomUserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create(request):
    user_data = request.data
    is_superuser = user_data.get('is_superuser', False) 

    if is_superuser:
        user = CustomUser.objects.create_superuser(
            email=user_data['email'],
            password=user_data['password'],
        )
    else:
        user = CustomUser.objects.create_user(
            email=user_data['email'],
            password=user_data['password'],
        )
    serializer = CustomUserSerializer(user)
    return Response(serializer.data)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update(request, user_id):
    user = CustomUser.objects.get(id = user_id)
    serializer = CustomUserSerializer(instance=user,data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
        user.delete()
        return Response({"message": "Note deleted successfully."}, status=204)
    except CustomUser.DoesNotExist:
        return Response({"message": "Note not found."}, status=404)