import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from ...models import *


@csrf_exempt
@require_http_methods(["POST"])
def create_group(request):
    data = json.loads(request.body)

    token = data.get("token")
    name = data.get("name")
    emails = data.get("emails")
    group_type = data.get('type')

    creator = User.objects.filter(token=token).first()
    if creator is None:
        return JsonResponse({"message": "User is None."}, status=400)

    members = User.objects.filter(email__in=emails)
    unregistered_members = emails
    for user in members:
        unregistered_members.remove(user.email)

    send_invitation_to_nonusers(unregistered_members)
    group_id = create_group_in_db(creator, name, group_type, members)

    return JsonResponse({"status": "Successfully created group.",
                         "group id": group_id,
                         "name": name,
                         "type": group_type,
                         "current members": [member.username for member in members],
                         "invitation sent to": unregistered_members})


def send_invitation_to_nonusers(emails):
    pass


def create_group_in_db(creator, name, type, members):
    group = Group(creator=creator, name=name, type=type)
    group.save()
    for user in members:
        print(user.email)
        group.members.add(user)
        group.save()
    return group.pk
