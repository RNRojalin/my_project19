from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
# Create your views here.

def topic(request):
    Qlto=Topic.objects.all()
    d={'Topic':Qlto}
    return render(request,'Display_topic.html',d)

def webpage(request):
    Qlwo=Webpage.objects.all()
    d={'Webpage':Qlwo}
    return render(request,'Display_webpage.html',d)

def accessrecord(request):
    Qlao=AccessRecord.objects.all()
    d={'AccessRecord':Qlao}
    return render(request,'Display_accessrecord.html',d)

def insert_topic(request):
    tn=input('enter Topic name')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    return HttpResponse('Topic is inserted successfully')

def insert_webpage(request):
    tn=input('enter Topic name')
    n=input('enter name')
    u=input('enter url')
    TO=Topic.objects.get(topic_name='Tennis')
    W=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    W.save()
    return HttpResponse('Webpage is inserted successfully')


def insert_accessrecord(request):
    n=input('enter name')
    db=input('enter date')
    a=input('enter author')
    WO=Webpage.objects.get(name='Sania Mirza')
    A=AccessRecord.objects.get_or_create(name=WO,date=db,author=a)[0]
    A.save()
    return HttpResponse('AccessRecord is inserted successfully')
