from django.urls import path
from .views import index, registro, nosotros, productos, administracion, ropa, coordinacion
from .views import usuarios, bodega, ventas, boleta, ingresar, usuarios, misventas,generar_informe
from .views import misdatos, miscompras, salir, carrito, ficha,masvendido,informar,misproductos
from .views import cambiar_estado_boleta, poblar, obtener_productos, eliminar_producto_en_bodega
from .views import premio, eliminar_producto_en_carrito, eliminar_fav,agregar_producto_al_carrito, favoritos
from .views import vaciar_carrito, mipassword, ver_producto,cambiar_password, comprar_ahora, comprar_carrito, aceptar_contrato

urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('registro', registro, name='registro'),
    path('nosotros', nosotros, name='nosotros'),
    path('productos/<accion>/<id>', productos, name='productos'),
    path('usuarios/<accion>/<id>', usuarios, name='usuarios'),
    path('cambiar_password', cambiar_password, name='cambiar_password'),
    path('bodega', bodega, name='bodega'),
    path('obtener_productos', obtener_productos, name='obtener_productos'),
    path('eliminar_producto_en_bodega/<bodega_id>', eliminar_producto_en_bodega, name='eliminar_producto_en_bodega'),
    path('ventas', ventas, name='ventas'),
    path('boleta/<nro_boleta>', boleta, name='boleta'),
    path('cambiar_estado_boleta/<nro_boleta>/<estado>', cambiar_estado_boleta, name='cambiar_estado_boleta'),
    path('ingresar', ingresar, name='ingresar'),
    path('misdatos', misdatos, name='misdatos'),
    path('mipassword', mipassword, name='mipassword'),
    path('miscompras', miscompras, name='miscompras'),
    path('salir', salir, name='salir'),
    path('carrito', carrito, name='carrito'),
    path('eliminar_producto_en_carrito/<carrito_id>', eliminar_producto_en_carrito, name='eliminar_producto_en_carrito'),
    path('vaciar_carrito', vaciar_carrito, name='vaciar_carrito'),
    path('agregar_producto_al_carrito/<producto_id>', agregar_producto_al_carrito, name='agregar_producto_al_carrito'),
    path('ficha/<producto_id>', ficha, name='ficha'),
    path('comprar_ahora', comprar_ahora, name='comprar_ahora'),
    path('comprar_carrito', comprar_carrito, name='comprar_carrito'),
    path('premio', premio, name='premio'),
    path('poblar', poblar, name='poblar'),
    path('administracion', administracion, name='administracion'),
    path('ropa', ropa, name='ropa'),
    path('favoritos', favoritos, name='favoritos'),
    path('masvendido', masvendido, name='masvendido'),
    path('informar', informar, name='informar'),
    path('misventas', misventas, name='misventas'),
    path('misproductos/<accion>/<id>', misproductos, name='misproductos'), 
    path('coordinacion', coordinacion, name='coordinacion'),
    path('generar-informe', generar_informe, name='generar_informe'),
    path('aceptar_contrato', aceptar_contrato, name='aceptar_contrato'),
    path('ver_producto', ver_producto, name='ver_producto'),
    path('eliminar_fav', eliminar_fav, name='eliminar_fav'),
]