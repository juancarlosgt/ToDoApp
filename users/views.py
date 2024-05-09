from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.serializers import serialize


def index(request):
    users = User.objects.all().exclude(is_superuser=True)
    data = serialize("python", users)
    return JsonResponse(data, safe=False)
