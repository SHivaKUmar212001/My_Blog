from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostDelete, PostUpdate, CustomLoginView
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path('login/', CustomLoginView.as_view(), name="login"),
   path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
   path('register/', views.register, name="register"),
   path('', PostList.as_view(), name="posts"),
   path('post/<int:pk>/',PostDetail.as_view(), name="post"),
   path('post-create/', PostCreate.as_view(), name="post-create"),
   path('post-delete/<int:pk>/', PostDelete.as_view(), name="post-delete"),
   path('post-update/<int:pk>/',PostUpdate.as_view(), name="post-update"),
]
