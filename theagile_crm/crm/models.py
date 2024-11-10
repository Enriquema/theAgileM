from django.db import models
from django.conf import settings


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, null=False, max_length=255)
    surname = models.CharField(blank=False, null=False, max_length=255)
    photo = models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')
    # We are not applying on_delete CASCADE in order to don't remove
    # Customers if we remove the related user
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='created_by', blank=True, null=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='updated_by', blank=True, null=True)
