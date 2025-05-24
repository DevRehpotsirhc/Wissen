from django.db import models

# Importo los modelos que requiero para las relaciones entre las tablas
from usuarios.models import Administrador, Docente, Estudiante
from faltas.models import Falta
    


# Tabla usada para el trigger de faltas y almacenar los IDs para generar el informe
class ListaChequeo(models.Model):
    id_lista_chequeo = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(Estudiante, on_delete=models.PROTECT, db_column="id_estudiante")
    id_docente = models.ForeignKey(Docente, on_delete=models.PROTECT, null=True, db_column="id_docente")
    id_administrador = models.ForeignKey(Administrador, on_delete=models.PROTECT, null=True, db_column="id_administrador")
    id_falta = models.ForeignKey(Falta, on_delete=models.PROTECT, db_column="id_falta")
    fecha_creacion = models.DateTimeField(auto_now_add=True)



# Modelo de Generador de Informes
class GenInfo(models.Model):
    id_gen_info = models.AutoField(primary_key=True)
    TIPOS = [
        ('csv', '.csv'),
        ('pdf', '.pdf'),
        ('word', '.docx'),
    ]
    tipo = models.CharField(max_length=4, choices=TIPOS, default='csv')
    id_lista_chequeo = models.ForeignKey(ListaChequeo, on_delete=models.PROTECT, db_column="id_lista_chequeo")
    id_docente = models.ForeignKey(Docente, on_delete=models.PROTECT, null=True, blank=True, db_column="id_docente")        # Docente o administrador que crea el informe se guardan sus credenciales para saber quién generó el informe
    id_administrador = models.ForeignKey(Administrador, on_delete=models.PROTECT, null=True, blank=True, db_column="id_administrador")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        autor = self.id_docente if self.id_docente is not None else self.id_administrador
        return f"ID: {self.id_gen_info}\nTipo de Exportación: {self.tipo}\nListado Utilizado: {self.id_lista_chequeo}\nAutor: {autor}\nFecha de Creación: {self.fecha_creacion.strftime('%d/%m/%y')}"