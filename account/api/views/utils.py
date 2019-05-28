from account.models import User


def get_user(func):

    def inner(request, *args, **kwargs):
        head = request.META
        token = head.get('HTTP_TOKEN').split()[1]
        user = User.objects.filter(token=token)

        if len(user) == 1:
            user = user.first()
        else:
            user = None

        return func(request, user, *args, ** kwargs)

    return inner


def send_invitation_to_nonusers(emails):
    pass


