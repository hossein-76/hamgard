import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from ...models import *


@require_http_methods(['POST'])
def log_out(request):
    data = json.loads(request.body)
    token = data.get('token')
    user = User.objects.filter(token=token).first()
    if user:
        user.logout_user()
        return JsonResponse({"message": "Successfully logged out."}, status=200)
    else:
        return JsonResponse({"message": "User not found."}, status=404)
