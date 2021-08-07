from django.urls import path
from app.views import home,about

urlpatterns =[
    path('',home.Home.as_view(), name="home"),
    path('about',about.Abouts.as_view(), name="about"),
]