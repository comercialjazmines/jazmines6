# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class Rol(models.Model):
    idrol = models.AutoField(primary_key=True)
    roltipo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rol'


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


class Usuariorol(models.Model):
    usuid = models.IntegerField()
    rol_idrol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='rol_idrol')

    class Meta:
        managed = False
        db_table = 'usuariorol'


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
