from django.urls import path
from . import views 
from core.views import login,nosotros
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('nosotros',views.nosotros,name='nosotros'),
    ]