from django.db import models

class Usuario(models.Model):
  email = models.EmailField(unique=True)
  first_name = models.CharField(max_length=150)
  last_name = models.CharField(max_length=150)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.first_name} {self.last_name} ({self.email})"

class Ingreso(models.Model):
  usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='ingresos')
  fecha_entrada = models.DateTimeField()
  fecha_salida = models.DateTimeField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"Ingreso de {self.usuario.username} - Entrada: {self.fecha_entrada} | Salida: {self.fecha_salida}"