from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from django.db.models import Q
from users import models, forms

# Create your views here.

def home(request):
    q = request.GET.get('q', '')
    users = found_posts = {}
    if q:
        users = User.objects.filter(
            Q(username__icontains=q)
        )
        found_posts = models.Posts.objects.filter(
            Q(title__icontains=q)
        )

    posts = models.Posts.objects.all()

    context = {
        'users': users, 'posts': posts,
        'found_posts': found_posts
        
    }
    return render(request, 'home/home.html', context)


def post(request, slug):
    
    #  user = get_object_or_404(User, username=user)
    post = get_object_or_404(models.Posts, slug=slug)
    comments = post.comments.all()
    form = {}
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            print(request.user)
            comment.post = post
            comment.save()
            return redirect(request.path_info)
    else:
        form = forms.CommentForm()
        return render(request, 'home/post_detail.html', {
            'post': post,
            'comments': comments,
            'form': form
            })

def post_delete(request, slug, id):
    # if request.method == 'POST':
    post = get_object_or_404(models.Posts, slug=slug, id=id)
    post.delete()
    return redirect('home')




def loginPage(request):
    # page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        un = request.POST.get('username').lower()
        pw = request.POST.get('password')
        try:
            user = User.objects.get(username=un)
        except Exception:
            print(Exception)
        user = authenticate(request, username=un, password=pw)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print(Exception)
            
            # messages.error(request, 'User does not exist!!!pw or un')

    # context = {'page': page}
    context = {}
    return render(request, 'home/login.html')


def registerUser(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create the user if the form is valid
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            # Create the user
            if User.objects.filter(username=username).exists():
                return redirect('register')
                
            user = User.objects.create_user(username=username.lower(), password=password, email=email)
            user.save()
            from users import models
            models.Profile.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'home/register.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('home')