from django.urls import path, include
from rest_framework import routers  
from empresas import views

router = routers.DefaultRouter()
router.register(r'empresas', views.EmpresaView,'empresas')

urlpatterns = [
    path("api/", include(router.urls))
   
]

