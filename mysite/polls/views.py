from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse

# Create your views here.


def index(request: WSGIRequest):
    print(type(request))
    return HttpResponse("Hello, world. You're at the polls index. ")
