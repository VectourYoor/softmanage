from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from Sell.models import *
from django.core.exceptions import ObjectDoesNotExist


def login(req):
    return render_to_response('login.html')


def index(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        try:
            rightps = User.objects.get(username=username).password
        except ObjectDoesNotExist:
            return HttpResponseRedirect('/login/')
        if password == rightps:
            req.session['username'] = username
            goods = Good.objects.all()
            return render_to_response('info.html', {'goods': goods})
        else:
            return HttpResponseRedirect('/login/')


def goodinfo(req):
    goodID = req.GET['goodID']
    return render_to_response('goodInfo.html')


def myinfo(req):
    username = req.session['username']
    return render_to_response('personInfo.html')


def talk(req):
    return render_to_response('talk.html')
