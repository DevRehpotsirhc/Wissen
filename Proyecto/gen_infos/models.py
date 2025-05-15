from django.db import models
from usuarios.models import Administrador, Docente, Estudiante


# Create your models here.
class GenInfo(models.Model):
    id_gen_info = models.AutoField(primary_key=True)
    id_tipo = models.ForeignKey('Tipo', on_delete=models.CASCADE)
    id_docente = models.ForeignKey('Docente', on_delete=models.CASCADE, null=True)
    id_admin = models.ForeignKey('Admin', on_delete=models.CASCADE, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.id_docente:
            return f"Info Docente: {self.id_docente}"
        elif self.id_admin:
            return f"Info Admin: {self.id_admin}"
        return f"GenInfo #{self.id_gen_info}"

class Tipo(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=5)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tipo