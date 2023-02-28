from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads,dumps
from math import gcd

# Create your views here.
class Fraccion:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    def toJSON(self):
        return dumps(self, default=lambda o:o.__dict__, sort_keys=False, indent=4)

def reduce(num,den):
    x=gcd(num,den)
    num= num // x
    den= den // x
    return Fraccion(str(num),str(den))

def index(request):
    #return HttpResponse('<h1> Bienvenidos a la sesión del jueves! </h1>')
    return render(request,'index.html')

def proceso(request):
    nombre = request.POST['nombre']
    nombre = nombre.upper()
    return HttpResponse('Hola '+ nombre)

def bienvenida(request):
    letrero="Bienvenida"
    return HttpResponse(letrero)

def multiplicacion(request):
    body_unicode =request.body.decode('utf-8')
    body = loads(body_unicode)
    n1=body['n1']
    d1=body['d1']
    n2=body['n2']
    d2=body['d2']
    
    p=int(n1)*int(n2)
    q=int(d1)*int(d2)
    resultado= reduce(p,q)
    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado,content_type ="text/json-comment-filtered")

@csrf_exempt
def suma(request):
    body_unicode =request.body.decode('utf-8')
    body = loads(body_unicode)
    n1=body['n1']
    d1=body['d1']
    n2=body['n2']
    d2=body['d2']
    
    n11=int(n1)
    n22=int(n2)
    d11=int(d1)
    d22=int(d2)
    if(d11==d22):
        p=n11+n22
        q=d11
    else:
        p=(n11*d22)+(n22*d11)
        q=d11*d22
    resultado= Fraccion(str(p),str(q))
    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado,content_type ="text/json-comment-filtered")

@csrf_exempt
def resta(request):
    body_unicode =request.body.decode('utf-8')
    body = loads(body_unicode)
    n1=body['n1']
    d1=body['d1']
    n2=body['n2']
    d2=body['d2']

    n11=int(n1)
    n22=int(n2)
    d11=int(d1)
    d22=int(d2)
    if(d11==d22):
        p=n11-n22
        q=d11
    else:
        p=(n11*d22)-(n22*d11)
        q=d11*d22
    resultado= reduce(p,q)
    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado,content_type ="text/json-comment-filtered")

@csrf_exempt
def division(request):
    body_unicode =request.body.decode('utf-8')
    body = loads(body_unicode)
    n1=body['n1']
    d1=body['d1']
    n2=body['n2']
    d2=body['d2']

    p=int(n1)*int(d2)
    q=int(d1)*int(n2)
    resultado= reduce(p,q)
    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado,content_type ="text/json-comment-filtered")
    #return HttpResponse("Division "+p+" / "+q+" = "+n)