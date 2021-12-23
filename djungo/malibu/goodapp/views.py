from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test(request):
    return render(request, 'goodapp/test.html' )

def aboutUs(request):
    return render(request, 'goodapp/aboutUs.html')

def Champagne(request):
    return render(request, 'goodapp/Champagne.html')

def Cognac(request):
    return render(request, 'goodapp/Cognac.html')

def login(request):
    return render(request, 'goodapp/login.html')

def PinkWine(request):
    title="Pink Wine"
    a1 = {'name': 'ARALDICA 20 Brachetto 20 frizzante' , 'image':'MarketImage/RoseWine/ARALDICA20Brachetto20frizzante-ROSE-8000.jpg' ,  'prize':'8000dollars'}
    a2 = {'name': 'carlo-rossi-Pink-Moscato','image':'MarketImage/RoseWine/carlo-rossi-Pink-Moscato-ROSE-3800.jpg','prize':'3800dollars'}
    a3 = {'name': 'Codorniu-ANNA-Rosado-ROSE','image':'MarketImage/RoseWine/Codorniu-ANNA-Rosado-ROSE-7000.jpg','prize':'7000dollars'}
    a4 = {'name': 'Herre-Rose', 'image': 'MarketImage/RoseWine/Herre-Rose-ROSE-8400.jpg', 'prize': '8400dollars'}
    a5 = {'name': 'rosa-assa-valey', 'image': 'MarketImage/RoseWine/rosa-assa-valey-ROSE-12000.jpg', 'prize' : '12000dollars'}


    alcho = [a1, a2, a3, a4, a5, ]

    dataMain = {"title": title, "alcho": alcho}

    return render(request, 'goodapp/PinkWine.html', context=dataMain)

def RedWine(request):
    return render(request, 'goodapp/RedWine.html')

def registration(request):
    return render(request, 'goodapp/registration.html')

def Rum(request):
    return render(request, 'goodapp/Rum.html')

def SparklingWine(request):
    return render(request, 'goodapp/SparklingWine.html')

def WhiteWine(request):
    return render(request, 'goodapp/WhiteWine.html')

def contact(request):
    return render(request, 'goodapp/contact.html')




