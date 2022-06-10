from django.db import models
from django.utils import timezone

# Create your models here.

class Pais(models.Model):
    idpais = models.AutoField(db_column='idPais', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, )  # Field name made lowercase.
    iso = models.CharField(db_column='ISO', max_length=2, )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pais'


class Estado(models.Model):
    idestado = models.AutoField(db_column='idEstado', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=25, )  # Field name made lowercase.
    iso = models.CharField(db_column='ISO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fk_pais = models.ForeignKey(Pais,on_delete= models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Estado'


class Mundeleg(models.Model):
    idmundeleg = models.AutoField(db_column='idMunDeleg', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, )  # Field name made lowercase.
    fk_estado = models.ForeignKey(Estado,db_column='fk_Estado' ,on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MunDeleg'

        
class Cp(models.Model):
    cp = models.AutoField(primary_key=True,db_column='cp')
    fk_mpiodel = models.ForeignKey(Mundeleg,db_column='fk_MpioDel', on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CP'

CHOICESUSER = [('Empleado','Empleado'),
               ('Visitante','Visitante')]

class Usuario(models.Model):

    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Correo', max_length=50, blank=True, null=True,unique=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rol = models.CharField(db_column='Rol', max_length=15,  blank=True, null=True, choices=CHOICESUSER)  # Field name made lowercase.
    fechacreacion = models.DateTimeField(db_column='fechaCreacion', blank=True, null=True,default=timezone.now)  # Field name made lowercase.
    fechaact = models.DateTimeField(db_column='fechaAct',default=timezone.now)  # Field name made lowercase.
    

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'Usuario'


class Personal(models.Model):
    idpersonal = models.AutoField(primary_key=True, db_column='idPersonal')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45,  blank=True, null=True)  # Field name made lowercase.
    paterno = models.CharField(db_column='Paterno', max_length=45,  blank=True, null=True)  # Field name made lowercase.
    materno = models.CharField(db_column='Materno', max_length=45,  blank=True, null=True)  # Field name made lowercase.
    genero = models.CharField(db_column='Genero', max_length=1,  blank=True, null=True)  # Field name made lowercase.
    fechanac = models.DateField(db_column='fechaNac', blank=True, null=True)  # Field name made lowercase.
    lugarnac = models.CharField(db_column='lugarNac', max_length=45,  blank=True, null=True)  # Field name made lowercase.
    rfc = models.CharField(db_column='RFC', max_length=13,  blank=True, null=True)  # Field name made lowercase.
    curp = models.CharField(db_column='CURP', max_length=18,  blank=True, null=True)  # Field name made lowercase.
    cel = models.CharField(db_column='Cel',  blank=True, null=True, max_length=10)  # Field name made lowercase.
    calle = models.CharField(db_column='Calle', max_length=45,  blank=True, null=True)  # Field name made lowercase.
    noint = models.IntegerField(db_column='noInt', blank=True, null=True)  # Field name made lowercase.
    noext = models.IntegerField(db_column='noExt', blank=True, null=True)  # Field name made lowercase.
    fk_usuario = models.ForeignKey(Usuario,db_column='fk_Usuario',on_delete=models.CASCADE, related_name='relacion_usuario')  # Field name made lowercase.
    fk_cp = models.ForeignKey(Cp,db_column='fk_Cp',on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Personal'


class Invitado(models.Model):
    idinvitado = models.AutoField(db_column='idInvitado', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45,  blank=True, null=True)  # Field name made lowercase.
    paterno = models.CharField(db_column='Paterno', max_length=45,  blank=True, null=True)  # Field name made lowercase.
    materno = models.CharField(db_column='Materno', max_length=45,  blank=True, null=True)  # Field name made lowercase.
    cargo = models.CharField(db_column='Cargo', max_length=60,  blank=True, null=True)  # Field name made lowercase.
    cel = models.CharField(db_column='Cel', max_length=12, blank=True, null=True)  # Field name made lowercase.
    orgprocedencia = models.CharField(db_column='orgProcedencia', max_length=60,  blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', blank=True, null=True, max_length=200)  # Field name made lowercase.
    fk_usuario = models.ForeignKey(Usuario,db_column='fk_Usuario',on_delete=models.CASCADE, related_name='relacion_usuarioI')  # Field name made lowercase.
    fk_mundeleg = models.ForeignKey(Mundeleg,db_column='fk_MunDeleg',on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Invitado'
