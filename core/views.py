from rest_framework import viewsets
from .serializers import UsuarioSerializer, IngresoSerializer
from .models import Usuario, Ingreso

class UsuarioViewSet(viewsets.ModelViewSet):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer

  def update(self, request, pk=None):
    try:
      usuario = self.get_object()
      serializer = self.get_serializer(usuario, data=request.data, partial=True)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response({"mensaje": "Usuario actualizado correctamente", "usuario": serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
      return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

  def destroy(self, request, pk=None):
    try:
      usuario = self.get_object()
      usuario.delete()
      return Response({"mensaje": "Usuario y sus ingresos fueron eliminados correctamente"}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
      return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class IngresoViewSet(viewsets.ModelViewSet):
  queryset = Ingreso.objects.all()
  serializer_class = IngresoSerializer