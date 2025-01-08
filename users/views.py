from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, PostUpdateForm
from .models import Posts

# @login_required
def user_profile(request, user):

    un = User.objects.get(username=user)
    user = get_object_or_404(User, username=user)
    profile = user.profile
    posts = un.posts.all()

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile', user=user)

    form = ProfileUpdateForm(instance=profile)

    photo_url = profile.photo.url if profile.photo else None
    return render(request, 'users/profile.html', {
        'profile': profile,
        'photo_url': photo_url,
        'form': form, 'posts': posts
        })


def create_post(request, user):
    if user == str(request.user):
        if request.method == 'POST':
            form = PostUpdateForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user  # Assign current user
                post.save()
                return redirect('home')  # or wherever you want to redirect after
        else:
            form = PostUpdateForm()
        return render(request, 'users/create-post.html', {'form': form})
    else:
        un = get_object_or_404(User, username=user)
        postts = Posts.objects.filter(user=un)
        return render(request, 'users/create-post.html',
                    {'posts': postts})

@login_required
def delete_acc(request, username, id):
    print(username, request.user)
    if username == str(request.user):
        if request.method == 'POST':
            try:
                user = User.objects.get(username=username, id=id)
                user.delete()
                return redirect('home')
            except Exception as e:
                print(f"Error deleting user: {str(e)}")
    