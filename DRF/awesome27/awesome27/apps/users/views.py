from django.http import response, JsonResponse
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response



class ping(View):
    def get(self, request):
        # return Response({'result' : 'pong'})
        return JsonResponse({"message": "pong"}, status=200)