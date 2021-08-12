from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from .models import Post
# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'blog1/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('posts')


class RegisterPage(FormView):
    template_name = 'blog1/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('posts')
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)

        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('posts')
        return super(RegisterPage, self).get(*args, **kwargs)

class PostList(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['posts'] = context['posts'].filter(user=self.request.user)
        context['count'] = context['posts'].filter().count()
        return context

class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post'

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','body']
    success_url = reverse_lazy('posts')
    def form_valid(self, form):
            form.instance.user = self.request.user
            return super(PostCreate, self).form_valid(form)

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog1/post_delete.html'
    success_url = reverse_lazy('posts')

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title','body']
    success_url = reverse_lazy('posts')
