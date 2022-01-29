from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from awesome27.apps.products.views import *
from rest_framework.routers import DefaultRouter


'''
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

urlpatterns = [
    path('/message', message_list),
    path('/message/<int:pk>', message_detail),
]
'''

'''
*위의 코드를 router로 구현할 수 있음

<router를 사용하는 이유>
    - viewset과 연계하여 url의 하드코딩을 막을수 있다.
    - as_view를 통해 각 request method마다 api를 연결시켜주었다면 router는 이를 알아서 연결해줌.
'''
router = DefaultRouter(trailing_slash=False)
router.register(r'/message', MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)),
]