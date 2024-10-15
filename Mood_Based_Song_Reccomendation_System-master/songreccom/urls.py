from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from .import views

urlpatterns=[
           path('',views.home,name='home'),
           path('songreccom/quiz',views.Quiz,name='quiz'),
           path('songreccom/quiz_result',views.result,name='result'),
           path('songreccom/about',views.about,name='about'),
           path('songreccom/contact',views.contact,name='contact'),
           path('registerpage',views.register,name="register"),
           path('login',views.login,name="login"),
           path('my_view',views.my_view,name="my_view")
           
] 