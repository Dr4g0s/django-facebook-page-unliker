from django.db import models
from allauth.socialaccount.models import SocialAccount


class FacebookPage(models.Model):
    account = models.ForeignKey(SocialAccount, on_delete=models.CASCADE)
    page_id = models.CharField(max_length=100)
    page_name = models.CharField(max_length=100)

    def __str__(self):
        return self.page_name
