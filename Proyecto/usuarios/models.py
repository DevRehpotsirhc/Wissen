from django.db import models

# Dar permisos de autenticación al modelo de Usuario
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



# Modelo que almacena todos los datos de una persona independientemente su rol
class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    IDEN = [
        ('ti', 'Tarjeta de Identidad'),
        ('ci', 'Cédula de Identidad'),
        ('ce', 'Cédula de Extrajería'),
        ('ppt', 'Permiso por Protección Temporal'),
    ]
    tipo_iden = models.CharField(max_length=3, choices=IDEN, default='ti')
    num_iden = models.CharField(max_length=12, unique=True)
    correo = models.EmailField(max_length=254)
    tel = models.CharField(max_length=15)
    # Se crea automático cuando se crea el registro
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        return f"ID: {self.id_persona}\nNombre: {self.nombre}\nApellidos: {self.apellidos}\nTipo de Identificación: {self.tipo_iden}\nNúmero de Identificación: {self.num_iden}\nCorreo: {self.correo}\nTeléfono: {self.tel}\nFecha de Creación: {self.fecha_creacion.strftime('%d/%m/%Y')}"



# Modelo que almacena los usuarios del sistema, y válida la autenticación
class UsuarioManager(BaseUserManager):
    def create_user(self, usuario, clave=None, **extra_fields):     # Al haber cambiado la valicación de usuarios de django por una personalizada se debe crear un UserManager con este método de creación
        if not usuario:
            raise ValueError('El nombre de usuario es obligatorio')
        
        user = self.model(usuario=usuario, **extra_fields)
        user.set_password(clave)
        user.save(using=self._db)

        return user

    def create_superuser(self, usuario, clave, **extra_fields):     # El superuser es obligatorio para Django aunque en este caso los superusers no se pueden crear mediante ningún registro, debido al control total, se deja como opción dentro de la propia base de datos, eso sin contar que ** NO SE ESTÁ USANDO EL ADMIN QUE INCLUYE DJANGO ** así que no se podría sacar partido de dicho usuario 
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(usuario, clave, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50, unique=True)

    ROLES = [
        ('admin', 'Administrador'),
        ('docen', 'Docente'),
        ('estud', 'Estudiante'),
    ]
    rol = models.CharField(max_length=5, choices=ROLES, default='estud')

    foto = models.CharField(max_length=250, blank=True, null=True)

    ESTADOS = [
        ('act', 'Activo'),
        ('ina', 'Inactivo'),
        ('rev', 'En Revisión'),
    ]
    estado = models.CharField(max_length=3, choices=ESTADOS, default='act')

    id_persona = models.ForeignKey('Persona', on_delete=models.CASCADE, db_column="id_persona")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # Campos requeridos por Django
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects: UsuarioManager = UsuarioManager()

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.usuario
    


# Modelo de administrador
class Administrador(models.Model):
    id_administrador = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column="id_usuario")
    CARGOS = [
        ('rec', 'Rector'),
        ('dir', 'Director'),
        ('cor', 'Coordinador'),
        ('adm', 'Administrador'),
    ]
    cargo = models.CharField(max_length=3, choices=CARGOS, default='adm')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        return f"ID: {self.id_administrador}\nUsuario: {self.id_usuario}\nCargo: {self.cargo}\nFecha de Creación: {self.fecha_creacion.strftime('%d/%m/%Y')}"
    


# Modelo de materias (matemáticas, física, química, etc)
class Materia(models.Model):
    id_materia = models.AutoField(primary_key=True)
    materia = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        return f"ID: {self.id_materia}\nMateria: {self.materia}\nFecha de Creación: {self.fecha_creacion.strftime('%d/%m/%Y')}"
    


# Modelo de cursos y/o grados (1ro, 2do, 3ro, etc)
class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    curso = models.CharField(max_length=50)
    JORNADA = [
        ('man', 'Mañana'),
        ('tar', 'Tarde'),
        ('noc', 'Noche'),
        ('sab', 'Sabatino'),
    ]
    jornada = models.CharField(max_length=50, choices=JORNADA, default='man')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        return f"ID: {self.id_curso}\nCurso: {self.curso}\nJornada: {self.jornada}\nFecha de Creación: {self.fecha_creacion.strftime('%d/%m/%Y')}"



# Modelo de docentes con relación con Materia y Curso
class Docente(models.Model):
    id_docente = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column="id_usuario")
    id_materia = models.ManyToManyField(Materia, related_name="docente_materia", db_column="id_materia")
    id_curso = models.ManyToManyField(Curso, related_name="docente_curso", db_column="id_curso")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        return f"ID: {self.id_docente}\nUsuario: {self.id_usuario}\nMaterias: {self.id_materia}\nCursos: {self.id_curso}\nFecha de Creación: {self.fecha_creacion.strftime('%d/%m/%Y')}"



# Modelo de estudiantes
class Estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column="id_usuario")
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE, db_column="id_curso")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    # Estructura de escritura que se mostrará al llamar al modelo
    def __str__(self):
        return f"ID: {self.id_estudiante}\nUsuario: {self.id_usuario}\nCurso: {self.id_curso}\nFecha de Creación: {self.fecha_creacion.strftime('%d/%m/%Y')}"