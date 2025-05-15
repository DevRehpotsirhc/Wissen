from django.db import models
from usuarios.models import Estudiante, Docente, Administrador

# Create your models here.
class Falta(models.Model):
    id_falta = models.AutoField(primary_key=True)
    id_tipo_falta = models.ForeignKey('TipoFalta', on_delete=models.CASCADE)
    desc = models.TextField()
    id_estudiante = models.ForeignKey('Estudiante', on_delete=models.CASCADE)
    id_docente = models.ForeignKey('Docente', on_delete=models.CASCADE, null=True)
    id_administrador = models.ForeignKey('Administrador', on_delete=models.CASCADE, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
        
    def __str__(self):
        # Devuelve una representación legible de la falta, incluyendo el estudiante, tipo de falta y fecha de creación
        return f"Falta de {self.id_estudiante} ({self.id_tipo_falta}) - {self.fecha_creacion}"

class TipoFalta(models.Model):
    id_tipo_falta = models.AutoField(primary_key=True)
    tipo_falta = models.CharField(max_length=10)
    fecha_creacion = models.DateTimeField()
    
    def __str__(self):
        return self.tipo_falta

class Justificacion(models.Model):
    id_justificacion = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey('Estudiante', on_delete=models.CASCADES)
    desc = models.TextField()
    archivo = models.CharField(max_length=250, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"Justificación de {self.id_estudiante} - {self.fecha_creacion}" 