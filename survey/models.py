from django.db import models


# Create your models here.

class Survey(models.Model):
    user = models.CharField(max_length=20)
    email = models.CharField(max_length=20)


    #def __str__(self):
    #    return f'[{self.pk}]{self.user}'
