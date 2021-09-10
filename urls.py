from django.urls import path
from .views import user_lists, user_login,user_profile,edit_user,delete_user,user_register

urlpatterns=[
    path("register/",user_register,name="Register User"),
    path("login/",user_login,name="Login User"),
    path("list/",user_lists,name="User list"),
    path("edit/<int:id>/",edit_user,name="edit_user"),
    path("profile/<int:id>/",user_profile,name="user_profile"),
    path("delete/<int:id>/",delete_user, name="delete_user")
]