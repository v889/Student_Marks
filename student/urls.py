from .views import *
from django.urls import path
urlpatterns=[
    path('',Signup.as_view(),name='signup'),
    path('login/',Login.as_view(),name='login'),
    path('home/',home,name='homepage'),
    path('result/',result,name='result'),
    path('logout/',logpout,name='logout'),

]