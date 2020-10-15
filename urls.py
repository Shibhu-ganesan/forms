from joinwithmeapp import views
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    path('startup/',views.startup, name='startup'),
    path('member/', views.member, name='member'),
    path('investor/', views.investor, name='investor'),

]