from django.urls import path
from .views.log_in import log_in
from .views.log_out import log_out
from .views.sign_up import sign_up
from .views.create_group import create_group
from .views.group_view import *

urlpatterns = [
    path('login/', log_in),
    path('logout/', log_out),
    path('signup/', sign_up),
    path('creategroup/', create_group),
    path('groups/', group_list),
    path('group/', group_detail)
]
