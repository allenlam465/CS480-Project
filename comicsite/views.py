from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from comicsite.models import Comic
from comicsite.models import Account
from comicsite.forms import AccountForm
from comicsite.forms import UserForm
from comicsite.forms import UserProfileForm
from django.urls import reverse


def home(request):
    return render(request, 'frontpage.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login credentials: {0}, {1}".format(username, password))
            return HttpResponse("Wrong username or password.")
    else:
        return render(request, 'loginpage.html', {})


def registered(request):
    return render(request, 'registered.html')


def register(request):
    isregistered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            isregistered = True

            return redirect('/registered')

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'registerpage.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


def user(request):
    return render(request, 'user.html')


def comic(request, pageid):
    comic = Comic.objects.filter(comicid=pageid)[0]

    context_dict = {'title': comic.comictitle,
                    'id': comic.comicid,
                    'author': comic.comicauthor,
                    'publisher': comic.comicpublisher,
                    'genre': comic.comicgenre,
                    'series': comic.comicseries,
                    'volume': comic.comicvolume,
                    'issue': comic.comicissue,
                    'rating': comic.comicrating,
                    'synopsis': comic.comicsynopsis,
                    'plot': comic.comicplot,
                    'cover': comic.comiccover}
    return render(request, 'comicpage.html', context_dict)


def account(request, userid):
    account = Account.objects.filter(accountid=userid)[0]

    context_dict = {'id': account.accountid,
                    'firstname': account.accountfirstname,
                    'lastname': account.accountlastname,
                    'email': account.accountemail,
                    'username': account.accountusername,
                    'password': account.accountpassword,
                    'city': account.accountcity,
                    'followid': account.followingid,
                    'picture': account.accountpicture}

    return render(request, 'user.html', context_dict)
#    return render(request, 'user.html')
