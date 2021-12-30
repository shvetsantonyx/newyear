from django.urls import path
from .views import *


urlpatterns = [
    path('', homepage, name='homepage'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('igor/', igor, name='igor'),
    path('roma/', roma, name='roma'),
    path('arti/', arti, name='arti'),
    path('alya/', alya, name='alya'),
    path('anton/', anton, name='anton'),
]