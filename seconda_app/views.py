from django.shortcuts import render
import datetime

# Create your views here.

def es_if(request):
    context = {
        'var1': 200,
        'var2': 200,
        'var3': 300
    }
    return render(request, "seconda_app/es_if.html", context)

def if_else_elif(request):
    context = {
        'var1': 100,
        'var2': 100.01,
        'var3': 100.50,
    }
    return render(request, "seconda_app/if_else_elif.html", context)

# Definisce una funzione di vista chiamata "es_for"
def es_for(request):
    # Crea un dizionario chiamato "context" che conterrà i dati da passare al template
    context = {
        # Lista 1: contiene un numero, una data e una stringa
        'list1': [1, datetime.date(2019, 7, 16), 'Non arrenderti!'],
        # Lista 2: uguale alla precedente, servirà per i cicli nel template
        'list2': [1, datetime.date(2019, 7, 16), 'Non arrenderti!']
    }
    
    # Restituisce la pagina HTML "es_for.html", passando il dizionario context
    return render(request, "es_for.html", context)

def index(request):
    return render(request,"seconda_app/index.html")