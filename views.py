
# Create your views here.
from django.shortcuts import render,redirect
from .forms import UserLogInForm, UserRegistrationForm
from .models import  User,RegisteredUser
# Create your views here.


def user_register(request):
       if request.method=="POST":
           form=UserRegistrationForm(request.POST,request.FILES)
           if form.is_valid():
               form.save()
           else:
               print(form.errors)    
       else:
            form=UserRegistrationForm()
       return render (request,"user_register.html",{"form":form})
def user_login(request):
       if request.method=="POST":
           form=UserLogInForm(request.POST,request.FILES)
           if form.is_valid():
               form.save()
           else:
               print(form.errors)    
       else:
            form=UserLogInForm()
       return render (request,"user_login.html",{"form":form})




def user_lists(request):
    users=User.objects.all
    return render(request,"user_list.html",{"users":users})   

def edit_user(request,id):
    user=User.objects.get(id=id)
    if request.method=="POST":
           form=UserRegistrationForm(request.POST,instance=user)
           if form.is_valid():
               form.save()
              
    else:
            form=UserRegistrationForm(instance=user)
    return render (request,"edit_user.html",{"form":form})   

def user_profile(request,id):
    user=UserLogInForm.objects.get(id=id)
    return render(request,"user_profile.html",{"user":user})   

def delete_user(request,id):
    user=User.objects.get(id=id)
    return render(request,"delete_user.html",{"user":user})   

def user_profile(request,id):
    user=User.objects.get(id=id)
    user.delete()
    return redirect(request,"user_list.html")   

         