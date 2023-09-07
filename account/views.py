from django.shortcuts import render
from .forms import LoginForm, UserRegistrationformm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def Login_User(request):
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(request, username= cd['username'], 
                                            password = cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponse("Athuticated Successfully")
                    else:
                        return HttpResponse("Disabled Account")
                else:
                    return HttpResponse("Invalid Login")
            
        else:
            form = LoginForm()
            return render(request, 'account/login.html', {'forms':form})
        
@login_required
def dashboard(request):
     return render(request, 'account/dashboard.html',{'section':'dashboard'})


def regester(request):
    if request.method == 'POST':
        user_form = UserRegistrationformm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )

            new_user.save()
            return render(request, 'account/registor_done.html', {'new_user': new_user})
        
    else:
        user_form = UserRegistrationformm()
        return render(request, 'account/register.html', {'user_form':user_form})
