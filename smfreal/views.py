from django.http import HttpResponse
from django.shortcuts import render
from smfreal.forms import UserForm, UserProfileInfoForm
from smfreal.models import fundlist


def index(request):
    return render(request,'smfreal/index.html')


def user_page(request):
    funddetail = fundlist.objects.order_by('fundno')
    fundd = {'fundl': funddetail }
    return render(request,'smfreal/fundlist.html',context=fundd)



def navbarfunction(request):
    return render(request,'smfreal/navigation.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfo

        if user_form.is_valid() and profile_form.is_valid():
            user = user-user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=false)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()


    return render(request,'smfreal/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})


def equity(request):
    funddetail = fundlist.objects.order_by('fundno')
    fundd = {'fundl': funddetail }
    return render(request,'smfreal/equity.html',context=fundd)

def debt(request):
    funddetail = fundlist.objects.order_by('fundno')
    fundd = {'fundl': funddetail }
    return render(request,'smfreal/debt.html',context=fundd)

def hybrid(request):
    funddetail = fundlist.objects.order_by('fundno')
    fundd = {'fundl': funddetail }
    return render(request,'smfreal/hybrid.html',context=fundd)
