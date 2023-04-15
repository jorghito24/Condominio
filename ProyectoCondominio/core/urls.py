from django.urls import path
from . import views
from core.views import login
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    ]