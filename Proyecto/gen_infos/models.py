from django.db import models

# Importo los modelos que requiero para las relaciones entre las tablas
from usuarios.models import Administrador, Docente, Estudiante
from faltas.models import Falta





# Modelo que identifica el tipo de documento de exportación (csv, word, pdf)
class Tipo(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=5)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        return f"ID: {self.id_tipo}\nTipo de Exportacion: {self.tipo}\nFecha de Creación: {self.fecha_creacion.strftime('%d/%m/%Y')}"
    


# Tabla usada para el trigger de faltas y almacenar los IDs para generar el informe
class ListaChequeo(models.Model):
    id_lista_chequeo = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    id_docente = models.ForeignKey(Docente, on_delete=models.CASCADE, null=True)
    id_administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE, null=True)
    id_falta = models.ForeignKey(Falta, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)



# Modelo de Generador de Informes
class GenInfo(models.Model):
    id_gen_info = models.AutoField(primary_key=True)
    id_tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    id_lista_chequeo = models.ForeignKey(ListaChequeo, on_delete=models.CASCADE)
    id_docente = models.ForeignKey(Docente, on_delete=models.CASCADE, null=True)        # Docente o administrador que crea el informe se guardan sus credenciales para saber quién generó el informe
    id_administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        autor = self.id_docente if self.id_docente is not None else self.id_administrador
        return f"ID: {self.id_gen_info}\nTipo de Exportación: {self.id_tipo}\nListado Utilizado: {self.id_lista_chequeo}\nAutor: {autor}\nFecha de Creación: {self.fecha_creacion.strftime('%d/%m/%y')}"