from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics 
from .serializer import InstructorsSerializer,CourseSerializer
from .models import Course,Instructor
from rest_framework.permissions import IsAuthenticated,IsAdminUser,BasePermission
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.authtoken.models import Token

 
# users = User.objects.all()

# for user in users:
#     token = Token.objects.get_or_create(user=user)
#     print(user.username)
#     print(token)


class WriteByAdminOnly(BasePermission):
    def has_permission(self,request,view):
        user = request.user
        if request.method == 'GET':
            return True

        if request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE':
            if user.is_superuser:
                return True
        return False


# Create your views here.
class InstructorListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes=[WriteByAdminOnly]
    serializer_class = InstructorsSerializer
    queryset = Instructor.objects.all()

class CourseListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes=[WriteByAdminOnly]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstructorsSerializer
    queryset = Instructor.objects.all()