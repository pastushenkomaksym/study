from django.http import JsonResponse

from .models import Student

def index(request):
    return JsonResponse({"msg": "University app"})
