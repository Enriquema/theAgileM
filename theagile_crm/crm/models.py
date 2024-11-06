from django.db import models
# from django.conf import settings


# class Customer(models.Model):
#     id = models.AutoField()
#     name = models.CharField(blank=False, null=False)
#     surname = models.CharField(blank=False, null=False)
#     photo = models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')
#     user = models.OneToOneField(settings.AUTH_USER_MODEL,
#                                 on_delete=models.CASCADE)

#     def __str__(self):
#         return f'Customer {self.name}'
