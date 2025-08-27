from django.shortcuts import render


from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>Hola Rosy 26 Curso de Django</h1>")



def acerca_de_mi(request):
    datos = {
        'Nombre': 'Rosy',
        'Edad': 40,
        'Trabajo': 'Cbtis114'
    }
    info = f"<h1>Acerca de mí</h1><p>Nombre: {datos['Nombre']}</p><p>Edad: {datos['Edad']}</p><p>Trabajo: {datos['Trabajo']}</p>"
    return HttpResponse(info)


def hola(request, primer_nombre):
    return HttpResponse(f"<h1>¡Hola, {primer_nombre}!</h1>")


def calcula_suma(request, num1, num2):
    resultado = num1 + num2
    return HttpResponse(f"<h1>La suma de {num1} + {num2} es {resultado}</h1>")