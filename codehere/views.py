from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Blog
from .models import Comment

# Create your views here.

def home_view(request):
    return render(request,'home.html')


def signup_view(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        re_password=request.POST.get('re_password')

        if password != re_password:
            return render(request,'signup.html',{
                'error':'invalid password'
            })

        if User.objects.filter(username=username).exists():
            return render(request,'signup.html',{
                'error':'username already exist'
            })


        User.objects.create_user(
            username=username,
            password=password
        )
        return redirect('login')
    return render(request,'signup.html')


def login_view(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user is not None:
         login(request,user)
         return redirect('dashboard')

        else:
         return render(request,'login.html',{
            'error':'invalid username or password'
        })

    return render(request,'login.html')


@login_required
def dashboard_view(request):

    blogs=Blog.objects.filter(user=request.user)

    return render(request, 'dashboard.html', {
        'user': request.user.username,
        'blogs': blogs
    })


def logout_view(request):
   logout(request)
   return redirect('home')



@login_required
def create_blog_view(request):

    if request.method == 'POST':

        title = request.POST.get('title')

        content = request.POST.get('content')

        visibility = request.POST.get('visibility')

        is_public = visibility == 'public'

        Blog.objects.create(
            user=request.user,
            title=title,
            content=content,
            is_public=is_public
        )

        return redirect('dashboard')

    return render(request, 'create_blog.html')





@login_required
def blog_detail_view(request, blog_id):

    blog = get_object_or_404(
        Blog,
        id=blog_id
    )

    if not blog.is_public and blog.user != request.user:
        from django.http import Http404
        raise Http404("Blog not found")

    comments = blog.comments.all().order_by('-created_at')

    return render(request, 'blog_detail.html', {
        'blog': blog,
        'comments': comments
    })





@login_required
def edit_blog_view(request, blog_id):

    blog = get_object_or_404(
        Blog,
        id=blog_id,
        user=request.user
    )

    if request.method == 'POST':

        blog.title = request.POST.get('title')

        blog.content = request.POST.get('content')

        blog.save()

        return redirect('blog_detail', blog_id=blog.id)

    return render(request, 'edit_blog.html', {
        'blog': blog
    })




@login_required
def delete_blog_view(request, blog_id):

    blog = get_object_or_404(
        Blog,
        id=blog_id,
        user=request.user
    )

    if request.method == 'POST':

        blog.delete()

        return redirect('dashboard')

    return redirect('blog_detail', blog_id=blog.id)




@login_required
def explore_blogs_view(request):

    blogs = Blog.objects.filter(is_public=True).select_related('user').order_by('-created_at')

    return render(request, 'explore_blogs.html', {
        'blogs': blogs
    })




@login_required
def profile_view(request, user_id):

    profile_user = get_object_or_404(
        User,
        id=user_id
    )

    blogs = Blog.objects.filter(
        user=profile_user,
        is_public=True
    ).order_by('-created_at')

    return render(request, 'profile.html', {
        'profile_user': profile_user,
        'blogs': blogs
    })




@login_required
def add_comment_view(request, blog_id):

    if request.method == 'POST':

        blog = get_object_or_404(
            Blog,
            id=blog_id,
            is_public=True
        )

        content = request.POST.get('content', '').strip()

        if content:
            Comment.objects.create(
                blog=blog,
                user=request.user,
                content=content
            )

        return redirect('blog_detail', blog_id=blog.id)

    return redirect('explore_blogs')
