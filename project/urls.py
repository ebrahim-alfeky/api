"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from app1.views import *


from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
# router=routers.DefaultRouter()
# router.register('',Student_view2)

# router1=routers.DefaultRouter()
# router1.register('',User_view)

Movie_Router=routers.DefaultRouter()
Movie_Router.register('',Movie_viewsets)

Reservation_Router=routers.DefaultRouter()
Movie_Router.register('',Reservation_viewsets)

Guest_Router=routers.DefaultRouter()
Guest_Router.register('',Guest_viewsets)

from app1.views import SignupView3,ChangePasswordView3
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)





urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('data/', data,name='data'),
    path('find_movie/', find_movie,name='find_movie'),
    path('new_reservation/', new_reservation,name='new_reservation'),
    
    path('movie/',Movie_Api.as_view(),name='movie'),
    path('movie/<int:id>/',Movie_Api.as_view(),name='one_movie'),
    path('movie_mixin/',Movie_Mixin_all.as_view(),name='movie_mixin'),
    path('movie_mixin/<int:pk>/',Movie_Mixin_one.as_view(),name='one_movie_mixin'),
    path('movie_generic/',Movie_generic_all.as_view(),name='movie_generic'),
    path('movie_generic/<int:pk>/',Movie_generic_one.as_view(),name='one_movie_generic'),
    path('movie_viewset/',include(Movie_Router.urls),name='movie_viewset'),

    
    path('guest/',Guest_Api.as_view(),name='guest'),
    path('guest_mixin/',Guest_mixix_all.as_view(),name='guest_mixin'),
    path('guest_mixin/<int:pk>/',Guest_mixix_one.as_view(),name='one_guest_mixin'),
    path('guest_generic/',Guest_generic_all.as_view(),name='guest_generic'),
    path('guest_generic/<int:pk>/',Guest_generic_one.as_view(),name='one_guest_generic'),
    path('guest_viewset/',include (Guest_Router.urls),name='guest_viewset'),

    path('reversation/',Reversation_Api.as_view(),name='reversation'),
    path('reversation_mixin/',Reservation_mixix_all.as_view(),name='reversation_mixin'),
    path('reversation_mixin/<int:pk>/',Reservation_mixix_one.as_view(),name='one_reversation_mixin'),
    path('reversation_generic/',Reversation_generic_all.as_view(),name='reversation_generic'),
    path('reversation_generic/<int:pk>/',Reservation_generic_one.as_view(),name='one_reversation_generic'),
    path('reservation_viewset/',include (Reservation_Router.urls),name='reservation_viewset'),

    # path('basic_auth/',include('rest_framework.urls')),#make logout option
    # path('token_auth/',obtain_auth_token)
    
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    
    path('token/signup/', SignupView2.as_view(), name='signup2'),
    path('token/login/', LoginView2.as_view(), name='login2'),
    path('token/logout/', LogoutView2.as_view(), name='logout2'),
    path('token/change_password/', ChangePasswordView2.as_view(), name='change_password2'),
    
    path('jwt/signup/', SignupView3.as_view(), name='signup'),
    path('jwt/login/', LoginView3.as_view(), name='jwt_login'),
    path('jwt/logout/', LogoutView3.as_view(), name='jwt_logout'),
    path('jwt/change-password/', ChangePasswordView3.as_view(), name='change_password'),
    # 🔐 JWT Auth built-in login/logout/refresh
    path('jwt/bulid_in_login/', TokenObtainPairView.as_view(), name='jwt_login'),
    path('jwt/bulid_in_refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('jwt/bulid_in_logout/', TokenBlacklistView.as_view(), name='jwt_logout'),
    
    
    path('cookie/',Cookie.as_view()),
    # path('students/',Student_view.as_view(),name='students'),
    # path('students/<int:id>/',Student_view.as_view(),name='one_student'),
    # path('students1/',include(router.urls)),
    # path('user/',include(router1.urls)),
    
    
]
