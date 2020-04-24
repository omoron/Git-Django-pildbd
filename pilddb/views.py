from django.shortcuts import render
from django.http import HttpResponse
from pilddb.models import Articulos
from django.conf import settings
from django.core.mail import send_mail
from pilddb.forms import FormContacts

# Create your views here.

def FindProducts(request):
    return render(request, "FindProducts.html")

def Find(request):
    if request.GET["prd"]:
        #msg = "Artículo buscado : %r" %request.GET["prd"]
        prod = request.GET["prd"]
        if len(prod) > 10:
            msg = "Texto de búsqueda no debe de exceder los 10 caracteres..!"
        else:
            art = Articulos.objects.filter(nombres__icontains = prod)
            return render(request, "FoundProducts.html", {"articulos" : art, "query" : prod})
    else:
        msg = "Debe ingresar un artículo para búsqueda..!"
    return HttpResponse(msg)

def Contact(request):
    #if request.method == "POST":
    #    subject = request.POST["asunto"]
    #    message = request.POST["mensaje"] + " " + request.POST["email"]
    #    email_from = settings.EMAIL_HOST_USER
    #    email_dest = ["oscar.moron.rosales@hotmail.com"]
    #    send_mail(subject, message, email_from, email_dest)
    #    return render(request, "Thanks.html")
    #return render(request, "Contacts.html")

    if request.method == "POST":
        fContacts = FormContacts(request.POST)
        if fContacts.is_valid():
            info = fContacts.cleaned_data
            send_mail(fContacts["subject"], fContacts["message"], info.get("email", ""), ["oscar.moron.rosales@hotmail.com"],)
    else:
        fContacts = FormContacts()
    return render(request, "FormContacts.html", {"form" : fContacts})