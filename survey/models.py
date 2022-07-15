from django.db import models


# Create your models here.

# python manage.py migrate --run-syncdb
# python manage.py runserver

class Survey(models.Model):
    user = models.CharField(max_length=20)
    age = models.CharField(max_length=20)

    survey = models.CharField(max_length=20)

    survey_num = models.IntegerField(null=True)



