from rest_framework import viewsets, permissions
from.models import Empresa
from .serializer import EmpresaSerializer




# Create your views here.
class EmpresaView(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.IsAuthenticated]
