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



# Modelo de la Falta con su descripción y usuarios relacionados
class Falta(models.Model):
    id_falta = models.AutoField(primary_key=True)
    TIPOS = [
        ('1','Leve'),
        ('2','Moderada'),
        ('3','Grave'),
    ]
    tipo_falta = models.CharField(max_length=1, choices=TIPOS, default="1")
    desc = models.TextField()
    id_estudiante = models.ForeignKey(Estudiante, on_delete=models.PROTECT, db_column="id_estudiante")
    id_docente = models.ForeignKey(Docente, on_delete=models.PROTECT, null=True, blank=True, db_column="id_docente")        # Se deja como null ya que una falta solo puede tener un docente o un administrador
    id_administrador = models.ForeignKey(Administrador, on_delete=models.PROTECT, null=True, blank=True, db_column="id_administrador")
    id_justificacion = models.ForeignKey(Justificacion, on_delete=models.PROTECT, null=True, blank=True, db_column="id_justificacion")        # La justificación de deja como null por si el estudiante no responde
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        return f"ID: {self.id_falta}\nTipo de Falta: {self.tipo_falta}\nDescripción: {self.desc}\nEstudiante: {self.id_estudiante}\nDocente: {self.id_docente}\nAdministrador: {self.id_administrador}\nFecha de Creación: {self.fecha_creacion.strftime('%d/%m/%Y')}"