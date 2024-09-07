from django.urls import path
from .views.login import signin
from .views.register import signup
from .views.home import home
from .views.users import users
from .views.update_user import update_user
from .views.accounts import accounts

urlpatterns = [
    path("login", signin , name="login"),
    path("register", signup , name="register"),
    path("update/<int:pk>", update_user , name="update_user"),
    path("", home , name="login"),
    path("users", users , name="users"),
    path("accounts", accounts , name="accounts"),

]