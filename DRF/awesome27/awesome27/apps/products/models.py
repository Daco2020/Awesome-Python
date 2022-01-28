from django.db import models
from awesome27.util.time_stamp import TimeStampModel
from awesome27.apps.users.models import User


class Message(TimeStampModel):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient')
    content = models.CharField(max_length=300)
    
    class Meta:
        db_table = 'messages'
        
