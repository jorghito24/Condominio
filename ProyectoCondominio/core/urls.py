from django.urls import path
from . import views 
from core.views import index,login, nosotros, vistadirectiva, vistaconserje, vistaresidente, pagoresidente
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('nosotros/',views.nosotros,name='nosotros'),
    path('vistadirectiva/',views.vistaresidente,name='vistadirectiva'),
    path('vistaconserje/',views.vistaresidente,name='vistaconserje'),
    path('vistaresidente/',views.vistaresidente,name='vistaresidente'),
    path('pagoresidente/',views.pagoresidente,name='pagoresidente')
    ]