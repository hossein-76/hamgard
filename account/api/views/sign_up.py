import json
from django.contrib.auth.hashers import make_password
from django.http.response import JsonResponse
from django.db.utils import IntegrityError
from django.views.decorators.http import require_http_methods
from ...models import User


@require_http_methods(['POST'])
def sign_up(request):
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
