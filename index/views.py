from django.shortcuts import render
from .models import kurser, books, om, plakater, about


# Create your views here.
def index(request):
    kurserliste = kurser.objects.all()
    plakatliste = plakater.objects.all().order_by('id')[:4]
    aboutliste = om.objects.all()
    bookliste = books.objects.all().order_by('id')[:3]
    return render(request, 'index.html', {"books": bookliste, "plakater": plakatliste, "navigation": kurserliste, "about": aboutliste})


def underside(request, slug):
    objekt = kurser.objects.get(slug=slug)
    kurserliste = kurser.objects.all()
    aboutliste = om.objects.all()
    return render(request, 'underside.html', {"undermenu": objekt, "navigation": kurserliste, "about": aboutliste})


def aboutdetailed(request, slug):
    objekt = om.objects.get(slug=slug)
    kurserliste = kurser.objects.all()
    aboutliste = om.objects.all()
    return render(request, 'omunderside.html', {"om": objekt, "navigation": kurserliste, "about": aboutliste})


def aboutinfo(request):
    objekt = about.objects.latest("id")
    kurserliste = kurser.objects.all()
    aboutliste = om.objects.all()
    return render(request, 'om.html', {"om": objekt, "navigation": kurserliste, "about": aboutliste})


def plakatside(request):
    objekt = plakater.objects.all()
    kurserliste = kurser.objects.all()
    aboutliste = om.objects.all()
    return render(request, 'plakater.html', {"plakater": objekt, "navigation": kurserliste, "about": aboutliste})


def books_and_articles(request):
    kurserliste = kurser.objects.all()
    objekt = books.objects.all()
    aboutliste = om.objects.all()
    return render(request, 'books.html', {"books": objekt, "navigation": kurserliste, "about": aboutliste})
