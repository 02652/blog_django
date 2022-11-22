from django.urls import path
from .views import CreatePost, DetailPost, HomeView, LoginUser, LogoutUser, RegisterUser, tagged

app_name = 'posts'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('register/', RegisterUser.as_view(), name="register"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', LogoutUser.as_view(), name="logout"),
    path('post/create/', CreatePost.as_view(), name="create_post"),
    path('post/<int:pk>/', DetailPost.as_view(), name="detail_post"),
    path('tag/<str:slug>', tagged, name="tagged"),

]
