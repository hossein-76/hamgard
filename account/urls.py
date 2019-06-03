from django.urls import path
from .authenticate import *


urlpatterns = [
    path('login/', login),
    path('logout/', logout),
    path('signup/', signup),

]
