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
from django.contrib import messages
# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'blog1/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('posts')


from .forms import CreateUserForm

def register(request):
    form=CreateUserForm()

    if request.method =="POST":
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context={'form':form}

    return render(request, 'blog1/register.html',context)

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
