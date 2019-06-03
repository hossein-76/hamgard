import django.contrib.auth as auth
import json
from django.contrib.auth.hashers import make_password
from django.http.response import JsonResponse
from django.db.utils import IntegrityError
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import *

@csrf_exempt
@require_http_methods(['POST'])
def login(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    remember_me = data.get("remember_me")
    user = auth.authenticate(username=username, password=password)
    if not user:
        return JsonResponse({"message": "incorrect username or password"}, status=400)
    if not remember_me:
        p = False
    else:
        p = True
    jwt_token = user.login_user(remember_me=p)
    return JsonResponse({"jwt_token": "token " + jwt_token}, status=200)


@csrf_exempt
@require_http_methods(['POST'])
def signup(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    phone_number = data.get('phone_number')
    user = User(username=username, password=make_password(password), mobile_number=phone_number)
    try:
        user.save()
    except IntegrityError:
        return JsonResponse({'message': "Username already taken."}, status=400)
    jwt_token = user.login_user(remember_me=False)
    return JsonResponse({'jwt_token': "token " + jwt_token})


@csrf_exempt
@require_http_methods(['POST'])
def logout(request):
    data = json.loads(request.body)
    token = data.get('token')
    user = auth.authenticate(token=token)
    if user:
        user.logout_user()
        return JsonResponse({"message": "Successfully logged out."}, status=200)
    else:
        return JsonResponse({"message": "User not found."}, status=404)
