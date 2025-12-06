from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from .form import RegisterForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import UpdateView

class UserLoginView(LoginView):
    template_name = "blog/login.html"
    authentication_form = AuthenticationForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "blog/register.html", {"form": form})


from django.views.generic import DeleteView
from django.urls import reverse_lazy

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# 
# UserPassesTestMixin


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # only author can update

from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user  # assign post to logged-in user
        return super().form_valid(form)


from django.views.generic import DetailView

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


# blog/views.py
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"   # HTML to display list
    context_object_name = "posts"


from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"   # your template
    context_object_name = "posts"
    ordering = ['-date_posted']             # latest first


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user   # set logged-in user as author
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author   # only author can edit


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author   # only author can delete
