from account.models import User
from django.http import JsonResponse
import smtplib


def get_user(func):
    """Utility decorator that gets the user of a request using provided token."""

    def inner(request, *args, **kwargs):
        head = request.META
        try:
            token = head.get('HTTP_TOKEN').split()[1]
        except AttributeError:
            return JsonResponse({"message": "token not provided in header."}, status=400)

        user = User.objects.filter(token=token)

        if len(user) == 1:
            user = user.first()
        else:
            return JsonResponse({"message": "user not found"}, status=404)

        return func(request, user, *args, ** kwargs)

    return inner


def send_invitation_to_nonusers(creator_name, group_name, other_members, emails):
    """Sends invitation message to emails that the group creator provides."""

    gmail_username = "hamgard.invitation@gmail.com"
    gmail_password = "Tahlil9798"
    try:

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(gmail_username, gmail_password)
    except Exception as e:
        print("unable to connect to server\nError text: {error_text}".format(error_text=e))
        return

    email_text = """
    You are receiving this email because {creator_name} has invited you to join him 
    in {group_name} group on Hamgard.

    Hamgard is an online tour and travel planner with exclusive offers on selected restaurants, cinemas, cafe's and ....

    Members currently in {group_name}:
    {other_members}

    visit Hamgard.com for more info.
        
    - Best regards
    - Hamgard development team
    """.format(creator_name=creator_name, group_name=group_name, other_members="\n\t".join(other_members))

    accepted_emails = check_mail_address(emails)
    for receiver in accepted_emails:
        try:
            server.sendmail(gmail_username, receiver, email_text)
            print('Email sent to {receiver}'.format(receiver=receiver))
        except Exception as e:
            print("ERROE: ", e)
    server.close()


def check_mail_address(emails):
    approved = []
    for email in emails:
        if email.find("..") != -1:
            continue

        if email.count("@") != 1:
            continue

        space_split = email.split()
        if len(space_split) > 1:
            continue

        at_split = email.split("@")
        if len(at_split) != 2:
            continue

        dot_split = at_split[1].split(".")
        if len(dot_split) != 2:
            continue
        approved.append(email)
    return approved
