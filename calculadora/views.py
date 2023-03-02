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

def procesamiento(request):
    nombre = request.POST['nombre']
    nombre = nombre.title()
    return render(request, 'proceso.html', {'name':nombre})

def bienvenida(request):
    letrero="Bienvenida"
    return HttpResponse(letrero)

@csrf_exempt
def multiplicacion(request):
    body_unicode =request.body.decode('utf-8')
    body = loads(body_unicode)
    numerador1=body['numerador1']
    denominador1=body['denominador1']
    numerador2=body['numerador2']
    denominador2=body['denominador2']
    
    p=int(numerador1)*int(numerador2)
    q=int(denominador1)*int(denominador2)
    resultado= reduce(p,q)
    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado,content_type ="text/json-comment-filtered")

@csrf_exempt
def suma(request):
    body_unicode =request.body.decode('utf-8')
    body = loads(body_unicode)
    numerador1=body['numerador1']
    denominador1=body['denominador1']
    numerador2=body['numerador2']
    denominador2=body['denominador2']
    
    numerador11=int(numerador1)
    numerador22=int(numerador2)
    denominador11=int(denominador1)
    denominador22=int(denominador2)
    if(denominador11==denominador22):
        p=numerador11+numerador22
        q=denominador11
    else:
        p=(numerador11*denominador22)+(numerador22*denominador11)
        q=denominador11*denominador22
    resultado= Fraccion(str(p),str(q))
    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado,content_type ="text/json-comment-filtered")

@csrf_exempt
def resta(request):
    body_unicode =request.body.decode('utf-8')
    body = loads(body_unicode)
    numerador1=body['numerador1']
    denominador1=body['denominador1']
    numerador2=body['numerador2']
    denominador2=body['denominador2']

    numerador11=int(numerador1)
    numerador22=int(numerador2)
    denominador11=int(denominador1)
    denominador22=int(denominador2)
    if(denominador11==denominador22):
        p=numerador11-numerador22
        q=denominador11
    else:
        p=(numerador11*denominador22)-(numerador22*denominador11)
        q=denominador11*denominador22
    resultado= reduce(p,q)
    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado,content_type ="text/json-comment-filtered")

@csrf_exempt
def division(request):
    body_unicode =request.body.decode('utf-8')
    body = loads(body_unicode)
    numerador1=body['numerador1']
    denominador1=body['denominador1']
    numerador2=body['numerador2']
    denominador2=body['denominador2']

    p=int(numerador1)*int(denominador2)
    q=int(denominador1)*int(numerador2)
    resultado= reduce(p,q)
    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado,content_type ="text/json-comment-filtered")
    #return HttpResponse("Division "+p+" / "+q+" = "+n)