from django.urls import path
from . import views
from .views import BlogCreate, CustomLoginView, BlogList, BlogDetail
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', BlogList.as_view(), name="blogs"),
    path('blog-create/', BlogCreate.as_view(), name="blog-create"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='blogs'), name="logout"),
    path('blog/<int:pk>/',BlogDetail.as_view(), name="blog"),
    path('register/', views.register, name="register"),
]
