from django.urls import path

from awesome27.apps.users.views import *

urlpatterns = [
    path('/ping', ping.as_view()),
]
