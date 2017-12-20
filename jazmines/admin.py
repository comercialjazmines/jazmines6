from django.contrib import admin
from .models import *
# Register your models here.

class RolAdmin(admin.ModelAdmin):
    list_display =('idrol','roltipo')

    class Meta:
    	model = Rol
    

admin.site.register(Rol, RolAdmin)


class UsuarioRolAdmin(admin.ModelAdmin):
    list_display = ("usuid", "rol_idrol",)

    class Meta:
    	model = UsuarioRol
    

admin.site.register(UsuarioRol, UsuarioRolAdmin)


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["cc_usuario", "nombre_usuario", "apellido_usuario", "pass_usuario","telefono_usuario", "direccion_usuario", "correo_usuario", ]

    class Meta:
        model = Usuario

admin.site.register(Usuario, UsuarioAdmin)


class ComunicacionesAdmin(admin.ModelAdmin):
    list_display = ["idcomunicaciones", "nombreusuario_comunicaciones", "correo_comunicaciones", "telefono_comunicaciones", "mensaje_comunicaciones" ]

    class Meta:
        model = Comunicaciones

admin.site.register(Comunicaciones, ComunicacionesAdmin)


class ContratoAdmin(admin.ModelAdmin):
    list_display = ["id_usuario_contrato", "oferta", "fecha_expiracion",]

    class Meta:
        model = Contrato

admin.site.register(Contrato, ContratoAdmin)


class EventosAdmin(admin.ModelAdmin):
    list_display = ["id_eventos", "nombre_evento", "lugar_evento", "fechainicio_evento","fechafin_evento"]

    class Meta:
        model = Eventos

admin.site.register(Eventos, EventosAdmin)


class ObituariosAdmin(admin.ModelAdmin):
    list_display = ["id_obituarios", "nombre_obituarios", "lugarvelacion_obituarios", "lugarexequias_obituarios", "lugardescanso_obituarios", "fechavelacion_obituarios", "fechaexequias_obituarios", "horavelacion_obituarios", "horaexequias_obituarios","horadescanso_obituarios"]

    class Meta:
        model = Obituarios

admin.site.register(Obituarios, ObituariosAdmin)


class PlanesAdmin(admin.ModelAdmin):
    list_display = ["id_plan", "nombre_plan", "cobertura_plan"]

    class Meta:
        model = Planes

admin.site.register(Planes, PlanesAdmin)


class SolicitudAdmin(admin.ModelAdmin):
    list_display = ["id_usuariosolicitud", "fecha_solicitud", "hora_solicitud"]

    class Meta:
        model = Solicitud

admin.site.register(Solicitud, SolicitudAdmin)


class TipoComunicacionAdmin(admin.ModelAdmin):
    list_display = ["idtipocomunicacion", "nombre_tipo"]

    class Meta:
        model = Tipocomunicacion

admin.site.register(Tipocomunicacion, TipoComunicacionAdmin)


class UsuariosNuevosAdmin(admin.ModelAdmin):
    list_display = ["idusuario_nuevo", "nombrecompleto_usuarionuevo", "telefono_usuarionuevo", "correo_usuarionuevo", "fecha_usuarionuevo", "hora_usuarionuevo"]

    class Meta:
        model = UsuariosNuevos

admin.site.register(UsuariosNuevos, UsuariosNuevosAdmin)
