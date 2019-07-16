from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from post.views import page_maker
# from django.contrib.contenttypes.models import ContentType

# Importng models
from comments.models import Comment
from django.contrib.auth.models import Group
from post.models import Tags, Post
from user_profile.models import UserProfile

# Importing Forms
from home.forms import UserSignupForm
from post.forms import PostForm
from comments.forms import CommentForm
User = get_user_model()
# A function to paginate posts and return them

HOME = '/'


def index(request):
    form = UserSignupForm()
    addpostform = PostForm()
    posts = page_maker(request)
    user_profiles = UserProfile.objects.all()
    tags = Tags.objects.all()

    # Using Model Manager all().
    comments = Comment.objects.all()
    comment_form = CommentForm()
    # if comment_form.is_valid():
    #     print(comment_form.cleaned_data)
    context = {
        'form': form,
        'addpostform': addpostform,
        'posts': posts,
        'tags': tags,
        'user_profiles': user_profiles,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'home/index.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Login Success")
            return redirect(HOME)
        else:
            messages.error(request, f"Login Failed")
            return redirect(HOME)
    else:
        return redirect(HOME)


def logout_view(request):
    logout(request)
    messages.success(request, f"Logout Success")
    return redirect(HOME)


def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            choice = form.cleaned_data.get('choice')
            user = authenticate(username=username, password=raw_password)
            if choice == 'teacher':
                my_group = Group.objects.get(name='Teacher')
                my_group.user_set.add(user)
                my_group.save()
            elif choice == 'student':
                my_group = Group.objects.get(name='Student')
                my_group.user_set.add(user)
                my_group.save()
            login(request, user)

            # Creating profile
            profile = UserProfile(user=user)
            profile.save()

            messages.success(request, f"Signup Success")
            return redirect(HOME)
    else:
        form = UserSignupForm()
    posts = page_maker(request)
    tags = Tags.objects.all()
    addpostform = PostForm()
    context = {
        'form': form,
        'addpostform': addpostform,
        'posts': posts,
        'tags': tags,
    }
    return render(request, 'home/index.html', context)
