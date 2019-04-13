from django.urls import path
from .views.log_in import log_in
from .views.log_out import log_out
from .views.sign_up import sign_up

urlpatterns = [
    path('login/', log_in),
    path('logout/', log_out),
    path('signup/', sign_up)
]
