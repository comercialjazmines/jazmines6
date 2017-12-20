
from django.conf.urls import include, url
from django.contrib import admin
from jazmines.views import *



urlpatterns = [
    # Examples:
    # url(r'^$', 'funerariajazmines.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', construccion, name="consruccion"),
    url(r'^inicio/$', index, name="index"),
    url(r'^acercadenosotros-enconstruccion/$', about, name="about"),
    url(r'^parquecementerio-enconstruccion/$', gallery, name="gallery"),
    url(r'^planesexequiales-enconstruccion/$', planes, name="planes"),
    url(r'^contacto-enconstruccion/$', contact, name="contacto"),
    url(r'^obituarios-enconstruccion/$', obituarios, name="obituarios"),
    url(r'^terminos-enconstruccion/$', terminos, name="terminos"),
    url(r'^login/$', login, name="login"),
    url(r'^alianzas-enconstruccion/$', alianzas, name="alianzas"),
    url(r'^sesion_obituarios/$', sesion_obituarios, name="sesion_obituarios"),
    url(r'^sesion_usuario/$', sesion_usuario, name="sesion_usuario"),
    url(r'^sesion_eventos/$', sesion_eventos, name="sesion_eventos"),
    url(r'^actualizar_noticias/$', actualizar_noticias, name="actualizar_noticias"),
    url(r'^agregar_obituarios/$', agregar_obituarios, name="agregar_obituarios"),
    url(r'^agregar_eventos/$', agregar_eventos, name="agregar_eventos"),
    url(r'^historico_obituarios/$', historico_obituarios, name="historico_obituarios"),
    url(r'^historico_eventos/$',historico_eventos, name="historico_eventos"),
    url(r'^modificar_eventos/$', modificar_eventos, name="modificar_eventos"),
    url(r'^modificar_obituarios/$', modificar_obituarios, name="modificar_obituarios"),
    url(r'^agregar_usuario/$', agregar_usuario, name="agregar_usuarios"),


]