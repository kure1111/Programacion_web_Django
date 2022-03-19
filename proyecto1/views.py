from multiprocessing import context
from urllib import request
from django.http import HttpResponse
import datetime as time
#from django.template import Template, Context, loader
from django.template.loader import get_template
from django.shortcuts import render
#primera vista

class person(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def Hola(request):
    p1 = person("Albert", "Garciaaaaaaaaaaa")
    fechita = time.datetime.now()
    cargo = ["director", "agente", "panadero"]

    #doc_externo = get_template('template.html')
    dicci = {"nombre":p1.nombre, "apellido":p1.apellido, "fecha":fechita, "cargos":cargo}
    #documento = doc_externo.render(dicci) 

    return render(request,
        'template.html',
        context=dicci)


#Vista 2
def Despedida(HRequest): 

    return HttpResponse("Ayosss")

#Dinámico
def fecha(request):
    fecha_hoy = time.datetime.now()
    #%s marcador de posicion    
    documento = """ <html5>
    <body>
    <h2>
    Esta es la hora %s 
    </h2>
    </body>
    </html5>""" % fecha_hoy
    return HttpResponse(documento)

def suma(request, a, b):
    c = a + b
    documento = """ <html5>
    <body>
    <h2>
    La suma de %s + %s es igual %s
    </h2>
    </body>
    </html5>""" % (a, b, c)

    return HttpResponse(documento)

def contenido(request):
    fecha_hoy = time.datetime.now()
    return render(request, "contenido.html", {"fecha":fecha_hoy})

def contenido2(request):
    fecha_hoy = time.datetime.now()
    return render(request, "contenido2.html", {"fecha":fecha_hoy})
