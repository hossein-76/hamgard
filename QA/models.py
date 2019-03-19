from django.db import models


# Create your models here.

class Question(models.Model):
    product = models.ForeignKey('product.Event', on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    approval_status = models.CharField(default="pending", max_length=10, choices=(("pending", "pending"),
                                                                                  ("approved", "approved"),
                                                                                  ("rejected", "rejected")))
    reason = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.text


class Answer(models.Model):
    agent = models.ForeignKey('account.Vendor', on_delete=models.CASCADE)
    answer = models.TextField(null=True, blank=True)
    approval_status = models.CharField(default="pending", max_length=10, choices=(("pending", "pending"),
                                                                                  ("approved", "approved"),
                                                                                  ("rejected", "rejected")))
    reason = models.TextField(null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.pk


class CommentImage(models.Model):
    alt = models.CharField(max_length=200)
    image = models.ImageField()


class Comment(models.Model):
    product = models.ForeignKey('product.Event', on_delete=models.CASCADE)
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    text = models.TextField()
    images = models.ManyToManyField('CommentImage', blank=True, related_name="comment_images")
    date = models.DateTimeField(null=True)
    approval_status = models.CharField(default='pending', max_length=20,
                                       choices=(('rejected', 'rejected'),
                                                ('approved', 'approved'),
                                                ('pending', 'pending'),
                                                ('old_version', 'old_version')))
    reject_reason = models.TextField(blank=True, null=True)
    validator = models.ForeignKey('account.Vendor', blank=True,
                                  related_name="validator",
                                  null=True, on_delete=models.SET_NULL)
    validate_date = models.DateTimeField(null=True, blank=True)
    user_ip = models.CharField(max_length=20, null=True, blank=True)
    is_buyed = models.BooleanField(default=False, null=True, blank=True)

    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return "id:{}".format(self.id)
