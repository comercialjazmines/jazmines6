# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Rol(models.Model):
    idrol = models.AutoField(primary_key=True)
    roltipo = models.CharField(max_length=50)

    def __str__(self):
        return str(self.roltipo)

    class Meta:
        managed = False
        db_table = 'rol'



class UsuarioRol(models.Model):
    usuid = models.ForeignKey(User)
    rol_idrol = models.ForeignKey(Rol)

    class Meta:
        managed = False
        db_table = 'usuariorol'




class Comunicaciones(models.Model):
    idcomunicaciones = models.AutoField(primary_key=True)
    nombreusuario_comunicaciones = models.TextField()
    correo_comunicaciones = models.TextField()
    telefono_comunicaciones = models.IntegerField()
    mensaje_comunicaciones = models.TextField()
    tipo_comunicacion_idtipo_comunicacion = models.ForeignKey('Tipocomunicacion', models.DO_NOTHING, db_column='TIPO_COMUNICACION_idTIPO_COMUNICACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comunicaciones'


class Contrato(models.Model):
    id_usuario_contrato = models.AutoField(primary_key=True)
    oferta = models.IntegerField()
    fecha_expiracion = models.DateField()
    planes_id_plan = models.ForeignKey('Planes', models.DO_NOTHING, db_column='PLANES_id_Plan', blank=True, null=True)  # Field name made lowercase.
    usuario_cc_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='USUARIO_cc_usuario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contrato'





class Eventos(models.Model):
    id_eventos = models.AutoField(primary_key=True)
    nombre_evento = models.TextField()
    lugar_evento = models.TextField()
    fechainicio_evento = models.DateField()
    fechafin_evento = models.DateField()
    usuario_cc_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='USUARIO_cc_usuario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventos'


class Obituarios(models.Model):
    id_obituarios = models.AutoField(primary_key=True)
    nombre_obituarios = models.TextField()
    lugarvelacion_obituarios = models.TextField()
    lugarexequias_obituarios = models.TextField()
    lugardescanso_obituarios = models.TextField()
    fechavelacion_obituarios = models.DateField(blank=True, null=True)
    fechaexequias_obituarios = models.DateField()
    horavelacion_obituarios = models.TimeField(blank=True, null=True)
    horaexequias_obituarios = models.TimeField()
    horadescanso_obituarios = models.TimeField(blank=True, null=True)
    usuario_cc_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='USUARIO_cc_usuario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'obituarios'


class Planes(models.Model):
    id_plan = models.AutoField(db_column='id_Plan', primary_key=True)  # Field name made lowercase.
    nombre_plan = models.TextField()
    cobertura_plan = models.TextField()

    class Meta:
        managed = False
        db_table = 'planes'





class Solicitud(models.Model):
    id_usuariosolicitud = models.AutoField(primary_key=True)
    fecha_solicitud = models.DateField()
    hora_solicitud = models.TimeField()
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitud'


class Tipocomunicacion(models.Model):
    idtipocomunicacion = models.AutoField(primary_key=True)
    nombre_tipo = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipocomunicacion'


class Usuario(models.Model):
    cc_usuario = models.IntegerField(primary_key=True)
    nombre_usuario = models.TextField()
    apellido_usuario = models.TextField(db_column='apellido_Usuario')  # Field name made lowercase.
    pass_usuario = models.IntegerField()
    telefono_usuario = models.IntegerField()
    direccion_usuario = models.TextField(blank=True, null=True)
    correo_usuario = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'





class UsuariosNuevos(models.Model):
    idusuario_nuevo = models.AutoField(primary_key=True)
    nombrecompleto_usuarionuevo = models.TextField()
    telefono_usuarionuevo = models.TextField()
    correo_usuarionuevo = models.TextField()
    fecha_usuarionuevo = models.DateField()
    hora_usuarionuevo = models.TimeField()

    class Meta:
        managed = False
        db_table = 'usuarios nuevos'
