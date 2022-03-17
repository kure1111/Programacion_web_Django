from multiprocessing import context
from unittest import loader
from django.http import HttpResponse
import datetime as time
from django.template import Template, Context, loader
from django.template.loader import get_template
#primera vista

class person(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def Hola(HttpRequest):
    p1 = person("Albert", "Garciaaaaaaaaaaa")
    fechita = time.datetime.now()
    cargo = ["director", "agente", "panadero"]
    #importante 3 pasos Template, Context, render 
    #doc_externo = open("C:/Users/kure/Documents/Git_proco/Django/proyecto1/proyecto1/template/template.html")
    #plt = Template(doc_externo.read())
    #doc_externo = loader.get_template('template.html')
    doc_externo = get_template('template.html')
    #llamamos la clave del diccionario en plantilla para acceder a la info
    #ctx = Context({"nombre":p1.nombre, "apellido":p1.apellido, "fecha":fechita, "cargos":cargo})
    #doc_externo.close()
    dicci = {"nombre":p1.nombre, "apellido":p1.apellido, "fecha":fechita, "cargos":cargo}
    documento = doc_externo.render(dicci) 

    return HttpResponse(documento)

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