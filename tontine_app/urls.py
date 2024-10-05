from django.urls import path
from .views.login import signin
from .views.register import signup
from .views.home import home
from .views.users import users
from .views.update_user import update_user
from .views.accounts import accounts
from .views.account_detail import account_detail
from .views.account_transaction import account_transation
from .views.deposit import deposit
from .views.withdraw import withdraw
from .views.withdraw_validation import withdraw_validation
from .views.add_account import add_account
from .views.user_home import user_home
from .views.user_account_detail import user_account_detail
from .views.manager import manager

urlpatterns = [
    path("login", signin , name="login"),
    path("register", signup , name="register"),
    path("update/<int:pk>", update_user , name="update_user"),
    path("", home , name="login"),
    path("users", users , name="users"),
    path("accounts", accounts , name="accounts"),
    path("account_detail/<int:pk>", account_detail , name="account_detail"),
    path("account_transaction/<int:pk>", account_transation , name="account_transaction"),
    path("deposit/<int:pk>", deposit , name="deposit"),
    path("withdraw/<int:pk>", withdraw , name="withdraw"),
    path("withdraw_validation", withdraw_validation , name="withdraw_validation"),
    path("add_account/<int:pk>", add_account , name="add"),
    path("user_home/<int:pk>", user_home , name="user_home"),
    path("user_account_detail/<int:pk>", user_account_detail , name="user_account_detail"),
    path("manager", manager , name="manager"),






]