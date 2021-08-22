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
from .models import Blogmodel
from django.contrib import messages
# Create your views here.


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

    return render(request, 'sblog/register.html',context)



class CustomLoginView(LoginView):
    template_name = 'sblog/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('blogs')




class BlogCreate(LoginRequiredMixin, CreateView):
    model = Blogmodel
    fields = ['title','body']
    success_url = reverse_lazy('')

class BlogList(ListView):
    model = Blogmodel
    template_name = 'sblog/frontpage.html'
    context_object_name = 'blogs'

class BlogDetail(DetailView):
    model = Blogmodel
    template_name = 'sblog/blogdetail.html'
    context_object_name = 'blog'
