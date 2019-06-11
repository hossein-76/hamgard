from django.urls import path, include


urlpatterns = [
<<<<<<< HEAD
    path('login/', login),
    path('logout/', logout),
    path('signup/', signup),

=======
    path('api/', include('account.api.urls'))
>>>>>>> cfa878d6c4fb6fad1aaac670a1296ed06788449e
]
