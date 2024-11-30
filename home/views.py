from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class Operation1(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,reuest):
        item=Student.objects.all()
        seriailizer=StudentSerializer(item,many=True)
        return Response(seriailizer.data,status=status.HTTP_200_OK)

class Operation2(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        try:
            user_obj=authenticate(username=username, password=password)
            if(user_obj):
                token, _ = Token.objects.get_or_create(user=user_obj)
                return Response(str(token),status=status.HTTP_200_OK)
            return Response("Invalid Credentialis",status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response("Invalid Student", status=status.HTTP_404_NOT_FOUND)

class Operation3(APIView):
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

