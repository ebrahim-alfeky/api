from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,BasePermission
from rest_framework import viewsets,status,mixins,generics,viewsets
from .serializer import*
from.models import*
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from rest_framework.pagination import PageNumberPagination

# Create your views here.

# class Student_view(APIView):
#     def get(self,request,id=0):
#         if id !=0:
#             student=Student.objects.filter(id=id).first()
#             student=Studentserializer(student)
#             return Response(student.data)
#         students=Student.objects.all()
#         students=Studentserializer(students,many=True)
#         return Response(students.data)
#     def post(self,request):
#         serializer = Studentserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save() 
#             return Response(serializer.data, status=status.HTTP_201_CREATED)  # إرجاع البيانات مع حالة نجاح
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # إرجاع الأخطاء لو البيانات غير
#     def put(self, request, id):
#         student = Student.objects.filter(id=id).first()
#         if not student:
#             return Response({"error": "Student not found"}, status=404)

#         serializer = Studentserializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, id):
#         student = Student.objects.filter(id=id).first()
#         if not student:
#             return Response({"error": "Student not found"}, status=404)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

        

# class Student_view2(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=Studentserializer
    
# class User_view(viewsets.ModelViewSet):
#     queryset=User.objects.all()
#     serializer_class=UserSerializer


@api_view(['GET','POST'])
def data(request):
    if request.method=='GET':
        movie=request.GET.get('movie')
        guest=request.GET.get('guest')
        reversation=request.GET.get('reversation')
        if movie:
            movies=Movie.objects.all()
            dic={}
            for movie in movies:
                dic[f'{movie.id}']=movie.movie
            return JsonResponse(dic, )
            ''''
            safe=False
دا ضروري لما تبعت ليست في JsonResponse،
لأن الوضع الطبيعي إنه يستنى dict.
            '''
            serializer=MovieSerializer(movies,many=True)
            return Response(serializer.data)
        if guest:
            guests=Guest.objects.all()
            dic={}
            for i in guests:
                dic[f'{i.id}']=i.name
            return JsonResponse(dic)
            serializer=GuestSerializer(guests,many=True)
            return Response(serializer.data)
        if reversation:
            reservations=Reservation.objects.all()
            list=[]
            for i in reservations:
                guests_data=[]
                movie_data=[]
                for j in i.guests.all():
                    guests_data.append({
                            "id":j.id,
                            "name":j.name
                        })
                for j in i.movies.all():
                    movie_data.append({
                            'id':j.id,
                            "movie":j.movie
                        })
                list.append({
                'id':i.id,
                'guests':guests_data,
                'movies':movie_data
                })
            return JsonResponse(list,safe=False)
            serializer=ReservationSerializer(reservations,many=True)
            return Response(serializer.data)
        return Response({"Enter query param to show data"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        movie=request.GET.get('movie')
        guest=request.GET.get('guest')
        reversation=request.GET.get('reversation')
        if movie:
            movie=MovieSerializer(data=request.data)
            if movie.is_valid():
                movie.save()
                return Response(movie.data,status=status.HTTP_201_CREATED)
            return Response({"error": "Enter valid data"}, status=status.HTTP_400_BAD_REQUEST)
        if guest:
            guest=GuestSerializer(data=request.data)
            if guest.is_valid():
                guest.save()
                return Response(guest.data,status=status.HTTP_201_CREATED)
            return Response({"error": "Enter valid data"}, status=status.HTTP_400_BAD_REQUEST)
        if reversation:
            reversation=ReservationSerializer(data=request.data)
            if reversation.is_valid():
                reversation.save()
                return Response(reversation.data,status=status.HTTP_201_CREATED)
            return Response({"error": "Enter valid data"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Enter query param to add "}, status=status.HTTP_400_BAD_REQUEST)

class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user and request.user.is_authenticated
     
class Movie_Api(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    def get(self,request,id=0):
        if id !=0:
            movie=get_object_or_404(Movie,id=id)
            movie=MovieSerializer(movie)
            return Response(movie.data,status=status.HTTP_200_OK)
        movies=Movie.objects.all()
        paginator=PageNumberPagination()
        movies=paginator.paginate_queryset(movies,request)
        serializer=MovieSerializer(movies,many=True)
        return paginator.get_paginated_response(serializer.data)
    def post(self,request):
        data={
            'hall':request.data.get('hall'),
            'movie':request.data.get('movie'),
            'created_by':request.user.id
        }
        movie=MovieSerializer(data=data)
        if movie.is_valid():
            movie.save()
            return Response(movie.data,status=status.HTTP_201_CREATED)
        return Response({"error": movie.errors}, status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,id):
        movie =get_object_or_404(Movie,id=id,created_by=request.user)
        data={
            'hall':request.data.get('hall'),
            'movie':request.data.get('movie'),
            'created_by':request.user.id
        }
        serializer = MovieSerializer(instance=movie, data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Enter valid data"}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        deleted = get_object_or_404(Movie,id=id,created_by=request.user)
        deleted.delete()
        return Response("Deleted", status=status.HTTP_204_NO_CONTENT)

class Guest_Api(APIView):
    def get(self,request,id=0):
        guests=Guest.objects.all()
        serializer=GuestSerializer(guests,many=True)
        return Response(serializer.data)
    def post(self,request):
        guest=GuestSerializer(data=request.data)
        if guest.is_valid():
            guest.save()
            return Response(guest.data,status=status.HTTP_201_CREATED)
        return Response({"error": "Enter valid data"}, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,id):
        guest = Guest.objects.filter(id=id).first()
        if guest:
            serializer = GuestSerializer(instance=guest, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Enter valid data"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"error": "Guest with this ID does not exist"}, status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,id):
        deleted = Guest.objects.filter(id=id).first()
        if deleted:
            deleted.delete()
            return Response("Deleted", status=status.HTTP_204_NO_CONTENT)        
        
        return Response({"error": "Guest with this ID does not exist"}, status=status.HTTP_404_NOT_FOUND)

class Reversation_Api(APIView):
    def get(self,request,id=0):
        reservations=Reservation.objects.all()
        serializer=ReservationSerializer(reservations,many=True)
        return Response(serializer.data)
    def post(self,request):
        reversation=ReservationSerializer(data=request.data)
        if reversation.is_valid():
            reversation.save()
            return Response(reversation.data,status=status.HTTP_201_CREATED)
        return Response({"error": "Enter valid data"}, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,id):
        reversation = Reservation.objects.filter(id=id).first()
        if reversation:
            serializer = ReservationSerializer(instance=reversation, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Enter valid data"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Reversation with this ID does not exist"}, status=status.HTTP_404_NOT_FOUND)    
    def delete(self,request,id):
        deleted = Reservation.objects.filter(id=id).first()
        if deleted:
            deleted.delete()
            return Response("Deleted", status=status.HTTP_204_NO_CONTENT)        
        
        return Response({"error": "Reveastion with this ID does not exist"}, status=status.HTTP_404_NOT_FOUND)

class Movie_Mixin_all(
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView
                    ):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    # applay permission and authentcation localy on spesific function or class
    permission_classes=[IsAuthenticatedOrReadOnly]
class Movie_Mixin_one(
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView
                    ):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    def get(self,request,pk):
        return self.retrieve(request)
    def put(self,request,pk):
        return self.update(request)
    def delete(self,request,pk):
        return self.destroy(request)

class Guest_mixix_all(
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView 
                    ):
    
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[]
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class Guest_mixix_one(
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    generics.GenericAPIView 
                    ):
    
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer
    def get(self,request,pk):
        return self.retrieve(request)
    def put(self,request):
        return self.update(request)
    def delete(self,request,pk):
        return self.destroy(request)

class Reservation_mixix_all(
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView 
                    ):
    
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class Reservation_mixix_one(
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    generics.GenericAPIView 
                    ):
    
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer
    def get(self,request,pk):
        return self.retrieve(request)
    def put(self,request):
        return self.update(request)
    def delete(self,request,pk):
        return self.destroy(request)

class Movie_generic_all(generics.ListCreateAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    
class Movie_generic_one(generics.RetrieveUpdateDestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
     
class Guest_generic_all(generics.ListCreateAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer
    
class Guest_generic_one(generics.RetrieveUpdateDestroyAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer

class Reversation_generic_all(generics.ListCreateAPIView):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer
    
class Reservation_generic_one(generics.RetrieveUpdateDestroyAPIView):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer

class Movie_viewsets(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

class Guest_viewsets(viewsets.ModelViewSet):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer

class Reservation_viewsets(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer

@api_view(['GET'])
def find_movie(request):
    movie=Movie.objects.filter(
        movie=request.data['name'],
        hall=request.data['place']
    )
    movie=MovieSerializer(movie,many=True)
    return Response(movie.data)

@api_view(['POST'])
def new_reservation(request):
    movie = Movie.objects.filter(
        movie=request.data['movie_name'],
        hall=request.data['movie_place']
    )
    
    guest = Guest.objects.create(
        name=request.data['guest_name'],
        mobile=request.data['guest_mobile']
    )
    
    # 1. أنشئ الـ reservation بدون guests أو movies
    reservation = Reservation.objects.create()
    
    # 2. ضيفهم باستخدام set()
    reservation.guests.set([guest])
    reservation.movies.set(movie)  # movie هنا ممكن يكون queryset أو list

    # 3. رجّع البيانات باستخدام Serializer
    serialized = ReservationSerializer(reservation)
    return Response(serialized.data)
    
    
    
    
    
#session authentication 
@method_decorator(csrf_exempt, name='dispatch')
@permission_classes([AllowAny])
class SignupView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=400)
        User.objects.create_user(username=username, password=password)
        return Response({"message": "User created successfully"}, status=201)

@method_decorator(csrf_exempt, name='dispatch')
@permission_classes([AllowAny])
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            django_login(request, user)  # لازم نستخدم اسم تاني علشان ما يتعارضش مع اسم الـ view
            return Response({"message": "Logged in"})
        return Response({"error": "Invalid credentials"}, status=400)
# X-CSRFToken: <your_csrf_token>

@method_decorator(csrf_exempt, name='dispatch')
@permission_classes([AllowAny])
class LogoutView(APIView):
    def post(self, request):
        django_logout(request)
        response=Response({"message": "Logged out"})
        response.delete_cookie('csrftoken')
        return response



#token authentication 
class SignupView2(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=400)
        user = User.objects.create_user(username=username, password=password)
        return Response({"message": "User created"})

class LoginView2(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            return Response({"message": "Logged in successfully", "token": token.key})
        return Response({"error": "Invalid credentials"}, status=400)
# Authorization: Token <token>

class LogoutView2(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response({"message": "Logged out successfully"})

class ChangePasswordView2(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        user = request.user
        if not check_password(old_password, user.password):
            return Response({"error": "Old password is incorrect."}, status=400)
        user.set_password(new_password)
        user.save()
        Token.objects.filter(user=user).delete()
        new_token = Token.objects.create(user=user)
        return Response({"message": "Password changed successfully.", "token": new_token.key})



#JWT authentication 
class SignupView3(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=400)
        user = User.objects.create_user(username=username, password=password)
        return Response({"message": "User created"})

class LoginView3(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({"error": "Invalid credentials"}, status=400)
# Headers:Authorization: Bearer <access_token>

class LogoutView3(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response({"error": "Refresh token is required"}, status=400)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logged out successfully"})
        except Exception as e:
            return Response({"error": "Invalid token or token already blacklisted"}, status=400)

class ChangePasswordView3(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        user = request.user
        if not check_password(old_password, user.password):
            return Response({"error": "Old password is incorrect."}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(new_password)
        user.save()
        return Response({"message": "Password changed successfully"})

class Cookie(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        name = request.data.get('name')
        age = request.data.get('age')

        response = Response({'message': 'Cookies set successfully'})
        
        response.set_cookie(
            key='name',
            value=name,
            max_age=60*60*24,     # يوم
            path='/',
            secure=False,         # خليه True في حالة HTTPS
            httponly=True,
            samesite='Lax'
        )

        response.set_cookie(
            key='age',
            value=age,
            max_age=60*60*24,
            path='/',
            secure=False,
            httponly=True,
            samesite='Lax'
        )

        return response

    def get(self, request):
        csrf_token = request.COOKIES.get('csrftoken')
        session_id = request.COOKIES.get('sessionid')
        name = request.COOKIES.get('name')
        age = request.COOKIES.get('age')

        return Response({
            'csrftoken': csrf_token,
            'sessionid': session_id,
            'name': name,
            'age': age
        })



# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json

# @csrf_exempt
# def webhook_listener(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body.decode("utf-8"))
#             event_type = data.get("event")

#             # هنا تقدر تعمل أي لوجيك أنت محتاجه حسب نوع الحدث
#             return JsonResponse({"status": "success", "event": event_type}, status=200)

#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)

#     return JsonResponse({"message": "GET not allowed"}, status=405)#


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# @csrf_exempt  # عشان GitHub يقدر يبعت POST من غير CSRF token
# def github_webhook(request):
#     if request.method == "POST":
#         try:
#             payload = json.loads(request.body)
#             # نطبع أو نخزن الداتا اللي جت
#             print("📩 Webhook Received:", payload)

#             # مثلًا: نجيب رسالة الكوميت
#             commit_message = payload.get("head_commit", {}).get("message", "No message")
#             print("✅ Commit Message:", commit_message)

#             return JsonResponse({"status": "ok", "commit_message": commit_message})
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)
#     else:
#         return JsonResponse({"error": "Invalid method"}, status=405)
@csrf_exempt
def github_webhook(request):
    if request.method == "POST":
        payload = json.loads(request.body.decode("utf-8"))
        print("📩 GitHub Payload:")
        print(json.dumps(payload, indent=2))  # يطبع بشكل مرتب
        return JsonResponse({"status": "ok", "commit_message": payload.get("head_commit", {}).get("message", "No mess000age")})
    return JsonResponse({"error": "GET not allowed"}, status=405)

