from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User


# Homepage Feed
def home(request):

    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'index.html', {
        'posts': posts
    })


# Profile Page
def profile(request, id):

    user = User.objects.get(id=id)

    profile = Profile.objects.get(user=user)

    posts = Post.objects.filter(user=user)

    followers = Follow.objects.filter(following=user).count()

    following = Follow.objects.filter(follower=user).count()

    return render(request, 'profile.html', {
        'profile': profile,
        'posts': posts,
        'followers': followers,
        'following': following
    })


# Create Post
def create_post(request):

    if request.method == 'POST':

        image = request.POST.get('image')

        caption = request.POST.get('caption')

        user = User.objects.first()

        Post.objects.create(

            user=user,

            image=image,

            caption=caption

        )

        return redirect('/')

    return render(request, 'create_post.html')

# Like Post
def like_post(request, id):

    post = Post.objects.get(id=id)

    user = User.objects.first()

    Like.objects.create(

        post=post,

        user=user

    )

    return redirect('/')


# Add Comment
def add_comment(request, id):

    if request.method == 'POST':

        post = Post.objects.get(id=id)

        text = request.POST.get('text')

        user = User.objects.first()

        Comment.objects.create(

            post=post,

            user=user,

            text=text

        )

    return redirect('/')


# Follow User
def follow_user(request, id):

    user_to_follow = User.objects.get(id=id)

    follower = User.objects.first()

    Follow.objects.create(

        follower=follower,

        following=user_to_follow

    )

    return redirect(f'/profile/{id}')

def profile(request, id):

    user = User.objects.get(id=id)

    posts = Post.objects.filter(user=user)

    followers = Follow.objects.filter(following=user).count()

    following = Follow.objects.filter(follower=user).count()

    context = {

        'profile_user': user,

        'posts': posts,

        'followers': followers,

        'following': following,

    }

    return render(request, 'profile.html', context)