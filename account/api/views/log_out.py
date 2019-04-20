import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from account.models import User


@require_http_methods(['POST'])
def log_out(request):
    data = json.loads(request.body)
    header = json.loads(request.header)
    token = header.get('token')
    emails = data.get("emails")
    creator = User.objects.filter(token=token).first()
    if creator:
        creator.logout_user()
        return JsonResponse({"message": "Successfully logged out."}, status=200)
    else:
        return JsonResponse({"message": "User not found."}, status=404)
