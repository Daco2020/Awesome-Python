from rest_framework import viewsets
from awesome27.apps.products.models import Message
from awesome27.apps.products.serializers import MessageSerializer

# Create your views here.

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer