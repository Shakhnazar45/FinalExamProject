from django.shortcuts import render, redirect
from django.http import HttpResponse
from goodapp import models
from .models import Market,User
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductForm
from django.views.generic.edit import UpdateView, DeleteView

# Create your views here.

def test(request):
    red = Market.objects.filter(name = 'rosa-assa-valey')
    redd = Market.objects.filter(name = 'Banfi-Colle-Pino-Toscana-IGT')
    rumm = Market.objects.filter (name = 'Angostura-1824-Premium-12-Y.O')
    cogn = Market.objects.filter  (name ='Hennessy-PARADIS-IMPERIAL-Cognac-07')
    pink = Market.objects.filter(name='ARALDICA 20 Brachetto 20 frizzante')
    reddd = Market.objects.filter(name='Almaviva-Red')
    rummm = Market.objects.filter(name='Angostura-1787-15-Y.O')
    cognn = Market.objects.filter(name='Hennessy-PARADIS-Cognac-07')

    DataDict = {'red':red,'redd':redd,'rumm':rumm,'cogn':cogn,'pink':pink,'reddd':reddd,'rummm':rummm,'cognn':cognn }

    return render(request, 'goodapp/test.html' ,context = DataDict)

def aboutUs(request):
    return render(request, 'goodapp/aboutUs.html')

def Products(request):
    products = Market.objects.all()
    return render(request, 'goodapp/Product.html',{'products':products })

def Champagne(request):

    Champs = Market.objects.filter(category='Champagne')
    DataCh = {'Champs': Champs}
    return render(request, 'goodapp/Champagne.html',context=DataCh)

def Cognac(request):


    Cogns = Market.objects.filter(category='Cognac')
    DataCogn = {"Cogns": Cogns}
    return render(request, 'goodapp/Cognac.html',context=DataCogn)

def login(request):
    return render(request, 'goodapp/login.html')

def PinkWine(request):
    title="Pink Wine"
    alcho =Market.objects.filter(category='Pink Wine')

    dataMain = {"title": title, "alcho": alcho}

    return render(request, 'goodapp/PinkWine.html', context=dataMain)

def RedWine(request):
    RedWine = Market.objects.filter(category='Red Wine')

    DataRed  = {"RedWine": RedWine}
    return render(request, 'goodapp/RedWine.html',context = DataRed)

def registration(request):
    return render(request, 'goodapp/registration.html')

def Rum(request):
    Rum =  Market.objects.filter(category='Rum')

    DataRum = {'Rum':Rum}

    return render(request, 'goodapp/Rum.html', context=DataRum)

def WhiteWine(request):
    White = Market.objects.filter(category='White Wine')

    DataWh = {'White': White}
    return render(request, 'goodapp/WhiteWine.html',context = DataWh)

def SparklingWine(request):
    Spark = Market.objects.filter(category='Sparkling Wine')
    DataSp = {"Spark" :Spark}
    return render(request, 'goodapp/SparklingWine.html',context = DataSp )

def contact(request):
    return render(request, 'goodapp/contact.html')

def Cart(request):
    return render(request, 'goodapp/Cart.html')


class ProfileView(TemplateView):
    template_name = 'goodapp/accounts/profile.html'


def createProduct(request):
    form = ProductForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('Products')
    return render(request, 'goodapp/CreateProduct.html', {'form': form})


def product(request, id):
    product = Market.objects.get(id=id)
    return render(request, 'goodapp/ProductDetails.html', {'product': product})


class ProductUpdateView(UpdateView):
    model = Market
    fields = ['name', 'price', 'category']
    success_url = '/Products'


class ProductDeleteView(DeleteView):
    model = Market
    success_url = '/Products'








