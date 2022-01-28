from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from awesome27.apps.products.views import *


message_list = MessageViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })

message_detail = MessageViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('', message_list, name='message-list'),
    path('<int:pk>', message_detail, name='message-detail'),
])
