from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'blog/register.html', {'error': 'Passwords do not match.'})

        if User.objects.filter(username=username).exists():
            return render(request, 'blog/register.html', {'error': 'Username already taken.'})

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        return redirect('dashboard')

    return render(request, 'blog/register.html')


@login_required
def dashboard_view(request):
    return render(request, 'blog/dashboard.html', {
        'user': request.user
    })


def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # or any other page
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'blog/login.html')



def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')  

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

@login_required
def add_post(request):
    form = PostForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('user_posts')

    return render(request, 'blog/add_post.html', {'form': form})


@login_required
def user_posts(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'blog/user_posts.html', {'posts': posts})