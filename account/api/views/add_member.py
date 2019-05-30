import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from ...models import *
from . import utils


@csrf_exempt
@require_http_methods(["POST"])
def add_member(request):
    data = json.loads(request.body)
    emails = data.get('emails')
    admin = utils.get_user(request)
    name = data.get('name')

    if admin is None:
        return JsonResponse({"message": "Group not found."}, status=400)

    group = Group.objects.filter(name=name).first()
    members = User.objects.filter(email__in=emails)
    unregistered_members = emails
    for user in members:
        unregistered_members.remove(user.email)
        group.members.add(user)
        group.save()

    utils.send_invitation_to_nonusers(unregistered_members)

    return JsonResponse({"status": "Successfully added members.",
                         "group id": group.pk,
                         "name": group.name,
                         "type": group.type,
                         "added members": [member.username for member in members],
                         "invitation sent to": unregistered_members})
