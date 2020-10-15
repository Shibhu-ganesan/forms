from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('startup/', views.startup_page, name="startup_page"),
    path('member/', views.member_page, name="member_page"),
    path('investor', views.investor_page, name="investor_page"),
    path('startup_form', views.startup_form, name="startup_form"),
    path('member_form', views.member_form, name="member_form"),
    path('investor_form', views.investor_form, name="investor_form"),

]
