from django.urls import path
from app import views
urlpatterns = [
    path('',views.index,name='index'),
    path('our-team',views.ourTeam,name='ourteam'),
    path('events',views.events,name='events'),
    path('colloquium',views.colloquium,name='colloquium'),
    path('hackonix',views.hackonix,name='hackonix'),
    path('qoc',views.qoc,name='qoc'),
]

