from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login ,logout



# Create your views here.

def loginView(request):
    return render(request,"member/login.html")

def signupView(request):
    return render(request,"member/signup.html")


def loginForm(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pass")
        
        user = authenticate(username = username , password = password )

        if user is not None:
            login(request,user)
            messages.add_message(request, messages.SUCCESS, 'HURRAY... LOGIN SUCCESSFULL !! ')
            return redirect("/movie/")

        else:
            messages.add_message(request, messages.ERROR, 'OHHO !!!!!!!! EMAIL OR PASSWORD IS NOT VALID . ')
            return redirect("/member/login/")
        
    else:
        messages.add_message(request, messages.ERROR, 'PLEASE LOGIN CORRECTLY.....')
        return redirect("/member/login/")



def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email= request.POST.get("email")
        pass1= request.POST.get("pass1")
        pass2= request.POST.get("pass2")
        f_name = request.POST.get("first_name")
        last_name= request.POST.get("last_name")

        # validationssssss
        if(not(len(pass1)>7 and not pass1.isalnum())):
            messages.add_message(request, messages.INFO, 'PASSWORD MUST BE LONGER THEN 8 CHARACTERS AND SHOULD CONTAIN A SYMBOL.')
            return redirect("/member/signup/")
        
        if(not(pass1==pass2)):
            messages.add_message(request, messages.INFO, 'YOU HAVE ENTERED WRONG PASSWORD.BOTH THE PASSWORD MUST BE SAME.')
            return redirect("/member/signup/")

        else:
            newUser = User.objects.create_user(username,email,pass1)
            newUser.first_name = f_name
            newUser.last_name = last_name
            newUser.save()
            return redirect("/member/login/")
    else:
        messages.add_message(request, messages.ERROR, 'PLEASE SIGN IN !!!!!')
        return redirect("/member/signup/")



def Logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'LOGOUT SUCCESSFUL')
    return redirect("/movie/")
