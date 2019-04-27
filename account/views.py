# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404,render_to_response,render
from django.urls import reverse
from .models import Labours,Employers,Feed
import json
from rest_framework import viewsets
from .serializers import FeedSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'structure/home.html')

def signup_L(request):
    return render(request, 'structure/signup_Labour.html')

def login_L(request):
    return render(request, 'structure/login_Labour.html')

def signup_E(request):
    return render(request, 'structure/signup_Employer.html')

def login_E(request):
    return render(request, 'structure/login_Emp.html')

def detL(request):
    name=request.POST['sname']
    con=request.POST['pnum']
    pass1=request.POST['pass1']
    id_no=request.POST['id_no']
    addr=request.POST['addr']
    q=Labours(l_name=request.POST['sname'],l_con_no=request.POST['pnum'],l_pass=request.POST['pass1'],l_id_no=request.POST['id_no'],l_addr=addr)
    q.save()
    return render(request,'structure/detL.html',{'name':name,'con':con,'pass1':pass1,'id_no':id_no,'addr':addr})

def detE(request):
    name=request.POST['sname']
    con=request.POST['pnum']
    pass1=request.POST['pass1']
    eml=request.POST['emailid']
    id_no=request.POST['id_no']
    q=Employers(e_name=name,e_con_no=con,e_pass=pass1,e_mail=eml,e_id_no=id_no)
    q.save()
    return render(request,'structure/detE.html',{'name':name,'con':con,'pass1':pass1,'eml':eml,'id_no':id_no})


def dashE(request):
    usern=request.POST['uname']
    pas=request.POST['psw']
    for q in Employers.objects.all():
        if(q.e_con_no == usern and q.e_pass==pas):
            return render(request,'structure/dashE.html',{'name':q.e_name,'labour':Labours})
    messages.error(request,'Invalid')
    return render(request,'structure/login_Emp.html')



def dashL(request):
    usern=request.POST['uname']
    pas=request.POST['psw']
    for q in Labours.objects.all():
        if(q.l_con_no == usern and q.l_pass==pas):
            return render(request,'structure/dashL.html',{'name':q.l_name})
    messages.error(request,'Invalid')
    return render(request,'structure/login_Labour.html')


def find(request,name):
    n_list=[]
    addr=request.POST['locality']
    for q in Labours.objects.all():
        if(q.l_addr == addr and q.pres == 1):
            n_list.append(q)

    return render(request,'structure/dashE.html',{'n_list':n_list,'name':name,})



class FeedViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

@csrf_exempt 
def saveData(request):
    if request.method == "POST":
        received_data = json.loads(request.body)
        e_con_no=received_data.get("e_con_no")
        l_con_no=received_data.get("l_con_no")
        comment=received_data.get("comment")
        feed=Feed()
        feed.e_con_no = e_con_no
        feed.l_con_no = l_con_no
        feed.comment = comment
        feed.save()
        return HttpResponse("Your response")

