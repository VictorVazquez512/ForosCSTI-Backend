from rest_framework import status
from rest_framework.response import Response
#from rest_framework.views import APIView
from rest_framework.decorators import api_view
from applications.users.models import User
from applications.users.api.serializer import UserSerializer, UserListSerializer

@api_view(['GET', 'POST'])
def user_api_view(request):

    # list
    if request.method == 'GET':
        # queryset
        users = User.objects.all().values('id','username','email','password')
        users_serializer = UserSerializer(users, many = True)

        return Response(users_serializer.data, status = status.HTTP_200_OK)

    # create
    elif request.method == 'POST':
        users_serializer = UserSerializer(data = request.data)

        # validation
        if users_serializer.is_valid(): 
            users_serializer.save()
            return Response({'message':'Usuario creado correctamente!'}, status = status.HTTP_201_CREATED)

        return Response(users_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def user_detail_api_view(request,pk):
    # queryset / consulta
    user = User.objects.filter(id = pk).first()
    
    # validation / validación
    if user:

        # retrive / recuperar
        if request.method == 'GET':
            users_serializer = UserSerializer(user)
            return Response(users_serializer.data, status = status.HTTP_200_OK)
        
        # update / actualizar
        elif request.method == 'PUT':
            users_serializer = UserSerializer(user,data = request.data)
            if users_serializer.is_valid():
                users_serializer.save()
                return Response(users_serializer.data, status = status.HTTP_200_OK)
            return Response(users_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        # delete / eliminar
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message':'Usuario eliminado correctamente!'}, status = status.HTTP_200_OK)

    return Response({'message':'No se ha encontrado un usuario con estos datos'}, status = status.HTTP_400_BAD_REQUEST)