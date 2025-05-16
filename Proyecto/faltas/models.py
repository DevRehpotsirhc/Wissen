from django.db import models

# Importo los modelos que requiero para las relaciones entre las tablas
from usuarios.models import Estudiante, Docente, Administrador





# Modelo de la tabla de Justificaciones, 
class Justificacion(models.Model):
    id_justificacion = models.AutoField(primary_key=True)
    desc = models.TextField()
    archivo = models.CharField(max_length=250, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        return f"ID: {self.id_justificacion}\nDescripción: {self.desc}\nRuta del Archivo: {self.archivo}\nFecha de Creación: {self.fecha_creacion.strftime('%d/%m/%Y')}" 



# Modelo de tipo de falta (leve, moderada, grave)
class TipoFalta(models.Model):
    id_tipo_falta = models.AutoField(primary_key=True)
    tipo_falta = models.CharField(max_length=10)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        return f"ID: {self.id_tipo_falta}\nTipo de Falta: {self.tipo_falta}\nFecha de Creación: {self.fecha_creacion.strftime('%d/%m/%Y')}"



# Modelo de la Falta con su descripción y usuarios relacionados
class Falta(models.Model):
    id_falta = models.AutoField(primary_key=True)
    id_tipo_falta = models.ForeignKey(TipoFalta, on_delete=models.CASCADE)
    desc = models.TextField()
    id_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    id_docente = models.ForeignKey(Docente, on_delete=models.CASCADE, null=True)        # Se deja como null ya que una falta solo puede tener un docente o un administrador
    id_administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE, null=True)
    id_justificacion = models.ForeignKey(Justificacion, on_delete=models.CASCADE, null=True)        # La justificación de deja como null por si el estudiante no responde
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        return f"ID: {self.id_falta}\nTipo de Falta: {self.id_tipo_falta}\nDescripción: {self.desc}\nEstudiante: {self.id_estudiante}\nDocente: {self.id_docente}\nAdministrador: {self.id_administrador}\nFecha de Creación: {self.fecha_creacion.strftime('%d/%m/%Y')}"