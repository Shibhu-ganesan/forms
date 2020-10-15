from django.shortcuts import render

# Create your views here.

def home(req):
    context = {}
    return render(req, 'dashboard.html', context)

def startup(req):
    context = {}
    return render(req, 'startup.html', context)

def investor(req):
    context = {}
    return render(req, 'investor.html', context)

def member(req):
    context = {}
    return render(req, 'member.html', context)