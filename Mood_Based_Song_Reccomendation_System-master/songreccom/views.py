from django.shortcuts import render,redirect,reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import*
import random
import json
import re
from django.http import JsonResponse
from django.http import HttpResponse
from .models import* 

# Create your views here.

def home(request):
    return render(request,'songreccom/home.html')

def Quiz(request):
    items=list(quiz.objects.all())
    random.shuffle(items)
    q=items[:10]
    strings=[]

    ################################ Error is because of json.loads(request.body)####################################
    if request.method == 'POST':
        print("yes")
        data = json.loads(request.body)
        print(data)
        print("good to go")
        try:
            for data in data:
                op = dataset.objects.get(option=data)
                emotion = op.emotion
                print(f"{emotion} : {data}")
                strings.append(emotion)

            print(strings)
            res_mood = ""
            hashmap = {}
            for string in strings:
                if string in hashmap:
                    hashmap[string]+=1
                else:
                    hashmap[string]=1
            max_freq=0
            max_string=" "
            for string in hashmap:
                if hashmap[string] >max_freq:
                    max_freq = hashmap[string]
                    max_string = string
            print(f" the highest frequesncy string is {max_string}")
            #######if u add any additional function or try to return something or u try to redirect u will get error

            ########################################################## here add mood to database   
            res_mood +=max_string

            curr_mood = mood()
            curr_mood.user = 'neha'
            curr_mood.mymood = res_mood
            curr_mood.save()
            # print("mood is:",mood)

        except dataset.DoesNotExist:
            print("no found")
        return JsonResponse({'message':'success'})
        
    context={'q':q}
    return render(request,'songreccom/quiz.html',context)
        
def result(request):
    det_mood = mood.objects.last()

    context = {'det_mood':det_mood}
    return render(request,'songreccom/result.html',context)

def about(request):
    return render(request,'songreccom/about.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            f_name = form.cleaned_data['f_name']
            l_name = form.cleaned_data['l_name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            send_mail('Contact Form',
                f'Name:{f_name}\t{l_name}\nMessage:{content}',
                'settings.EMAIL_HOST_USER',
                [email],
                fail_silently = False,

                )
    context = {'form':form}
    return render(request,'songreccom/contact.html',context)

def register(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    #     form=CreateUserForm()
    #     if request.method=="POST":
    #         form=CreateUserForm(request.POST)
    #         if form.is_valid():
    #            form.save()
    #            user=form.cleaned_data.get('username')
    #            messages.success(request,"Account created successfully for"+" "+user)
    #            return redirect('login')
    

    # context={'form':form}
    return render(request,'songreccom/register.html') 


def login(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    #     if request.method=='POST':
    #         username=request.POST.get('username')
    #         password=request.POST.get('password')

    #         user=authenticate(request,username='username',password='password')
        
    #         if user is not None:
    #            login(request,user)
    #            return redirect('home')
    #         else:
    #            messages.info(request,"username or password is incorrect")
    
    context={}
    return render(request,'songreccom/login.html',context)

def logout(request):
    logout(request)
    return redirect('login')

def my_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        return JsonResponse('hello there')