from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from .forms import CommentForm, PostCreateForm, UserRegisterForm
from .models import Author, Comment, Post
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


class RegisterUser(View):
    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        #phone = formset_factory(PhoneNumberForm, extra=2)
        context = {
            'form': form,
            # 'phone': phone
        }
        return render(request, 'users/register.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if request.POST['password1'] == request.POST['password2']:
                form = UserRegisterForm(request.POST)
                if form.is_valid():
                    req = request.POST
                    user = Author.objects.create_user(
                        name=req['name'], username=req['username'], account_twitter=req['account_twitter'], description=req['description'],
                        street=req['street'], number=req['number'], door=req['door'], postal_code=req['postal_code'], city=req['city'], password=req['password1'])
                    user.save()
                    login(request, user)

                    return redirect('posts:home')
                else:
                    for msg in form.errors:
                        messages.error(request, form.errors[msg])

                    context = {
                        'form': form
                    }

                    return render(request, 'users/register.html', context)
            else:
                form = UserRegisterForm(request.POST)
                context = {
                    'form': form,
                    'error': 'Contraseña no igual'
                }
                return render(request, 'users/register.html', context)


class LogoutUser(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('posts:home')


class LoginUser(View):
    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        context = {
            'form': form
        }

        return render(request, 'users/login.html', context)

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm()
        if request.method == 'POST':
            user = authenticate(
                request, username=request.POST['username'], password=request.POST['password'])

            if user is None:
                context = {
                    'form': form,
                    'error': 'Username or password incorrect'
                }

                return render(request, 'users/login.html', context)
            else:
                login(request, user)
                return redirect('posts:home')


class CreatePost(View):
    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        context = {
            'form': form
        }
        return render(request, 'posts/create.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = PostCreateForm(request.POST)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.author = request.user
                new_post.save()
                form.save_m2m()

                return redirect('posts:home')


class HomeView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'posts/index.html', context)


class DetailPost(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm()
        comments = Comment.objects.filter(post=post)
        context = {
            'post': post,
            'form': form,
            'comments': comments
        }
        return render(request, 'posts/detail.html', context)

    def post(self, request, pk):
        if request.method == 'POST':
            post = get_object_or_404(Post, pk=pk)
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.author = request.user
                new_comment.post = post
                new_comment.save()

                return redirect('posts:detail_post', pk=pk)
