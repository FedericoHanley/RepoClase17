from django.http import HttpResponse #Sirve para devolver una respuesta http
import datetime
from django.template import Context, Template

def saludar(request): #(el request es una solicitud que envia el cliente)
    return HttpResponse ('Hola mundo!') #(Aca le envio la respuesta)

def segunda_vista (request):
    return HttpResponse ('<h2> esto es html!!! </h2>')

def dia_de_hoy (request):
    dia = datetime.datetime.today()
    cadena = 'Hoy es ' + str(dia)
    return HttpResponse (cadena)

def saludo_nombre (request,nombre):
    return HttpResponse ('Hola ' + nombre)

def calcula_nacimiento(request,edad):
    anio_nacimiento = 2022 - int(edad)
    cadena = ('Usted nacio en el anio ' + str(anio_nacimiento))
    return HttpResponse (cadena)

#creo la view donde llamo mi template1
def probandoHtml(request):
    mi_archivo = open('C:/Users/Dell/Desktop/Clase17/Proyecto1/Plantillas/template1.html') #abro el archivo que es de texto pero debo leerlo
    contenido = mi_archivo.read #Esto luego sera de otra forma mas simple
    mi_archivo.close() #Aca lo cierro porque ya quedo en contenido el codigo. Debo transformarlo en plantilla
    plantilla = Template(contenido) #Lo importe. es una clase 
    contexto = Context() #Aca voy a mandarle datos a partir de la proxima clase del curso. por ahora va vacio
    documento = plantilla.render(contexto)
    return HttpResponse(documento) #agrego comentario para una prueba commit