from django.core.urlresolvers import reverse
from .forms import SignUpForm,LoginForm,Post
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Blog


def sign_up_view(request):
    form = SignUpForm(request.POST or None)
    context = {
        "title":"Sign up form",
        "form":form
    }

    if request.method == "POST":
        form = SignUpForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("blog:login"))
    return render(request,"blog/signup.html", context=context)


def login_view(request):
    form = LoginForm(request.POST)

    if request.method == 'POST':
        # print(form.is_valid())

        if form.is_valid():
            username = form.cleaned_data['username']
            password_val = form.cleaned_data['password']
            print (username,password_val)
            user = authenticate(username=username, password=password_val)
            print(user)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse("blog:home"))
            else:
                messages.warning(request, "Invalid credentials, please try with valid credentials")

    context = {
        "title": "Login",
        "form": form,
    }

    return render(request,"blog/login.html", context=context)


def home(request):

    form = Post(request.POST)

    blog = Blog.get_top_10()

    context = {
        "title":"welcome home",
        "form":form,
        "blogs":blog,
    }
    print(form)

    return render(request,"blog/home.html", context=context)