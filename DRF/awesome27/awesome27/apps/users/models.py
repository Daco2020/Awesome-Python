from django.db import models
from awesome27.util.time_stamp import TimeStampModel


class User(TimeStampModel):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=300)
    
    class Meta:
        db_table = 'users'