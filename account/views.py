from django.shortcuts import render
from .forms import LoginForm, UserRegistrationformm,UserEditForm, ProfileEditForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
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
            Profile.objects.create(user = new_user)
            return render(request, 'account/registor_done.html', {'new_user': new_user})
        
    else:
        user_form = UserRegistrationformm()
        return render(request, 'account/register.html', {'user_form':user_form})
    
@login_required
def UserEdit(request):
    if request.method == 'POST':
        user_form    = UserEditForm(instance= request.user, data = request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data= request.POST, files=request.FILES)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated '\
                                      'successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form   = UserEditForm(instance=request.user)
        profile_form= ProfileEditForm(instance=request.user.profile)

    
    return render(request, 'account/user_edit.html', {'user_form':user_form,
                                                 'profile_form':profile_form})
