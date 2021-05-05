from django.urls import path

from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('kurser-og-certificeringer/<slug>',
         views.underside, name='underside'),
    path('boeger-og-artikler', views.books_and_articles, name='boeger'),
    path('plakater', views.plakatside, name='plakater'),
    path('om-sprogin/<slug>', views.aboutdetailed, name='omsprogindetailed'),
    path('om-sprogin', views.aboutinfo, name='omsprogin'),

]
