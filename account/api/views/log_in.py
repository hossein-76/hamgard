import json

from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(['POST'])
def log_in(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    remember_me = data.get("remember_me")
    user = authenticate(username=username, password=password)
    if not user:
        return JsonResponse({"message": "incorrect username or password"}, status=400)
    if not remember_me:
        p = False
    else:
        p = True
    token = user.login_user(remember_me=p)
    return JsonResponse({"jwt_token": "token " + token}, status=200)
