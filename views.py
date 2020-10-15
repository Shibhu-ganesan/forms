from django.shortcuts import render, redirect
from .Forms import *


def dashboard(request):
    context = {}
    return render(request, "joinwithmeapp/dashboard.html", context)


def startup_page(request):
    context = {}
    return render(request, "joinwithmeapp/startup_page.html", context)


def member_page(request):
    context = {}
    return render(request, "joinwithmeapp/member_page.html", context)


def investor_page(request):
    context = {}
    return render(request, "joinwithmeapp/investor_page.html", context)


def startup_form(request):
    form = StartUpForm()
    if request.method == "POST":
        form = StartUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {"form": form}
    return render(request, 'joinwithmeapp/startup_form.html', context)


def member_form(request):
    form = MemberForm()
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {"form": form}

    return render(request, 'joinwithmeapp/member_form.html', context)


def investor_form(request):
    form = InvestorForm()
    if request.method == "POST":
        form = InvestorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {"form": form}

    return render(request, 'joinwithmeapp/investor_form.html', context)
