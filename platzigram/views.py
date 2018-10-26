#Django
from django.http import HttpResponse
import json

#utilidades
from datetime import datetime

#Route for numbers in text
def hello(request):
    # now = datetime.now()
    # import pdb; pdb.set_trace()
    numbers = request.GET['numbers']
    return HttpResponse(str(numbers), content_type="application/json")

#Say hi
def hola(request):
    return HttpResponse("Hola")

#Say hi whith HTML
def index(request):
    return HttpResponse("<h1>Hoy una etiqueta HTML</h1>")

#return a json with the data of the request
def getPrueba1(request):
    numbers = [int(i) for i in request.GET["numbers"].split(",")]
    sorted_int = sorted(numbers)
#   [int (i) for i in numbers.split(",")]
#   import pdb; pdb.set_trace()
    data = {
        "status": "ok",
        "numbers": sorted_int,
        "message": "Numbers sorted"
    }
    print(numbers)
    return HttpResponse(json.dumps(data,indent=4),content_type="application/json")

#Say hi a user with the data of the request GET
def say_hi(request,name,age):
    if age < 18:
        message = "Sorry {} you are a little kid".format(name)
    else:
        message = "Welcome Mr. {}".format(name)
    return HttpResponse(message)
