from django.db import models



# Modelo de Tipo de Identificación
class TipoIden(models.Model):
    id_tipo_iden = models.AutoField(primary_key=True)
    tipo_iden = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        return f"Tipo de Identificación: {self.tipo_iden}\nFecha de Creación: {self.fecha_creacion.strftime('%d/%m/%Y')}"



# Modelo de Roles (Administrador, Docente, Estudiante)
class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        return f"Rol: {self.rol}\nFecha de Creación: {self.fecha_creacion.strftime('%d/%m/%Y')}"



# Modelo de Estado en el sistema (Activo, Inactivo, En revisión)
class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        return f"Estado en el Sistema: {self.estado}\nFecha de Creación: {self.fecha_creacion.strftime('%d/%m/%Y')}"



# Modelo que almacena todos los datos de una persona independientemente su rol
class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    id_tipo_iden = models.OneToOneField(TipoIden, on_delete=models.CASCADE)
    num_iden = models.CharField(max_length=12, unique=True)
    '''                     IMPORTANTE
    
    Hay que probar lo del related_name
    
    '''
    id_rol = models.ManyToManyField(Rol, related_name="persona_rol")
    foto = models.CharField(max_length=250)
    correo = models.EmailField(max_length=254)     # Válida el formato del correo
    tel = models.CharField(max_length=50)
    id_estado = models.OneToOneField(Estado, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        # Validar tipo de identificación y darle un nombre dependiendo el id que tenga
        # Validar tipo estado y darle un nombre dependiendo el id que tenga
        return f"Nombre: {self.nombre}\nApellido: {self.apellidos}\nTipo de Identificación: {self.id_tipo_iden}\nNúmero de Identificación: {self.num_iden}\nRol: {self.id_rol}\nRuta de la Foto: {self.foto}\nCorreo: {self.correo}\nTeléfono: {self.tel}\nEstado en el Sistema: {self.id_estado}\nFecha de Creación: {self.fecha_creacion.strftime('%d/%m/%Y')}"



# Modelo que almacena los usuarios del sistema
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50, unique=True)
    clave = models.CharField(max_length=255)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        return f"Usuario: {self.usuario}\nClave: {self.clave}\nPersona: {self.id_persona}\nFecha de Creación: {self.fecha_creacion.strftime("%d/%m/%Y")}"



# Modelo de cargos administrativos (rector, subdirector, director, etc)
class Cargo(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    cargo = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        return f"Cargo: {self.cargo}\nFecha de Creación: {self.fecha_creacion.strftime("%d/%m/%Y")}"
    


# Modelo de administrador y superuser del sistema
class Administrador(models.Model):
    id_administrador = models.AutoField(primary_key=True)
    id_usuario = models.ManyToManyField(Usuario, related_name="administrador")
    id_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        return f"Usuario: {self.id_usuario}\nCargo: {self.id_cargo}\nFecha de Creación: {self.fecha_creacion.strftime("%d/%m/%Y")}"
    


# Modelo de materias (matemáticas, física, química, etc)
class Materia(models.Model):
    id_materia = models.AutoField(primary_key=True)
    materia = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        return f"Materia: {self.materia}\nFecha de Creación: {self.fecha_creacion.strftime("%d/%m/%Y")}"



# Modelo de materias (matemáticas, física, química, etc)
class Jornada(models.Model):
    id_jornada = models.AutoField(primary_key=True)
    jornada = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        return f"Jornada: {self.jornada}\nFecha de Creación: {self.fecha_creacion.strftime("%d/%m/%Y")}"
    


# Modelo de cursos y/o grados (1ro, 2do, 3ro, etc), con relación 1 a muchos con jornada
class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    curso = models.CharField(max_length=50)
    id_jornada = models.ForeignKey(Jornada, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        return f"Curso: {self.curso}\nJornada: {self.id_jornada}\nFecha de Creación: {self.fecha_creacion.strftime("%d/%m/%Y")}"



# Modelo de docentes con relación con Materia y Curso
class Docente(models.Model):
    id_docente = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_materia = models.ManyToManyField(Materia, related_name="docente_materia")
    id_curso = models.ManyToManyField(Curso, related_name="docente_curso")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        return f"Usuario: {self.id_usuario}\nMaterias: {self.id_materia}\nCursos: {self.id_curso}\nFecha de Creación: {self.fecha_creacion.strftime("%d/%m/%Y")}"



# Modelo de estudiantes con relación 1 a muchos entre Curso
class Estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        return f"Usuario: {self.id_usuario}\nCurso: {self.id_curso}\nFecha de Creación: {self.fecha_creacion.strftime("%d/%m/%Y")}"