import sqlite3
from django.contrib.auth.models import User, Permission
from django.db import connection
from datetime import date, timedelta
from random import randint
from core.models import Categoria, Producto, Carrito, Perfil, Boleta, DetalleBoleta, Bodega

def eliminar_tabla(nombre_tabla):
    conexion = sqlite3.connect('db.sqlite3')
    cursor = conexion.cursor()
    cursor.execute(f"DELETE FROM {nombre_tabla}")
    conexion.commit()
    conexion.close()

def exec_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)

def crear_usuario(username, tipo, nombre, apellido, correo, es_superusuario, 
    es_staff, rut, direccion, subscrito, imagen):

    try:
        print(f'Verificar si existe usuario {username}.')

        if User.objects.filter(username=username).exists():
            print(f'   Eliminar {username}')
            User.objects.get(username=username).delete()
            print(f'   Eliminado {username}')
        
        print(f'Iniciando creación de usuario {username}.')

        usuario = None
        if tipo == 'Superusuario':
            print('    Crear Superuser')
            usuario = User.objects.create_superuser(username=username, password='123')
        else:
            print('    Crear User')
            usuario = User.objects.create_user(username=username, password='123')

        if tipo == 'Administrador':
            print('    Es administrador')
            usuario.is_staff = es_staff
            
        usuario.first_name = nombre
        usuario.last_name = apellido
        usuario.email = correo
        usuario.save()

        if tipo == 'Administrador':
            print(f'    Dar permisos a core y apirest')
            permisos = Permission.objects.filter(content_type__app_label__in=['core', 'apirest'])
            usuario.user_permissions.set(permisos)
            usuario.save()
 
        print(f'    Crear perfil: RUT {rut}, Subscrito {subscrito}, Imagen {imagen}')
        Perfil.objects.create(
            usuario=usuario, 
            tipo_usuario=tipo,
            rut=rut,
            direccion=direccion,
            subscrito=subscrito,
            imagen=imagen)
        print("    Creado correctamente")
    except Exception as err:
        print(f"    Error: {err}")

def eliminar_tablas():
    eliminar_tabla('auth_user_groups')
    eliminar_tabla('auth_user_user_permissions')
    eliminar_tabla('auth_group_permissions')
    eliminar_tabla('auth_group')
    eliminar_tabla('auth_permission')
    eliminar_tabla('django_admin_log')
    eliminar_tabla('django_content_type')
    #eliminar_tabla('django_migrations')
    eliminar_tabla('django_session')
    eliminar_tabla('Bodega')
    eliminar_tabla('DetalleBoleta')
    eliminar_tabla('Boleta')
    eliminar_tabla('Perfil')
    eliminar_tabla('Carrito')
    eliminar_tabla('Producto')
    eliminar_tabla('Categoria')
    #eliminar_tabla('authtoken_token')
    eliminar_tabla('auth_user')

def poblar_bd(test_user_email=''):
    eliminar_tablas()
    
    crear_usuario(
        username='nzamora',
        tipo='Cliente', 
        nombre='Nicolas', 
        apellido='Zamora', 
        correo=test_user_email if test_user_email else 'nic.zamora@duocuc.cl', 
        es_superusuario=False, 
        es_staff=False, 
        rut='20612698-1',	
        direccion='5121 Esopo, Pedro Aguirre Cerda, \nSantiago 82000 \nChile', 
        subscrito=True, 
        imagen='perfiles/niczam.jpg'
    )

    crear_usuario(
        username='d.munoz',
        tipo='Cliente', 
        nombre='Danae', 
        apellido='Munoz', 
        correo=test_user_email if test_user_email else 'd.munozo@duocuc.cl', 
        es_superusuario=False, 
        es_staff=False, 
        rut='234779295',	
        direccion='233 La Victoria, Villa Sur, \nSantiago 2431 \nChile', 
        subscrito=True, 
        imagen='perfiles/dmunozo.png'
    )

    crear_usuario(
        username='tleithon',
        tipo='Cliente', 
        nombre='Tom', 
        apellido='Leithon', 
        correo=test_user_email if test_user_email else 't.leithon@duocuc.cl', 
        es_superusuario=False, 
        es_staff=False, 
        rut='22319199-k',	
        direccion='102 Renca, Colina, \nSantiago 232 101 \nChile', 
        subscrito=True, 
        imagen='perfiles/tleithon.jpg'
    )

    crear_usuario(
        username='czamora',
        tipo='Cliente', 
        nombre='Claudia', 
        apellido='Zamora', 
        correo=test_user_email if test_user_email else 'c.zamora@duocuc.cl', 
        es_superusuario=False, 
        es_staff=False, 
        rut='24870967-7',	
        direccion='202 Pudahuel, Laguna Sur, \nSantiago 40202 \nChile', 
        subscrito=True, 
        imagen='perfiles/czamora.jpg'
    )

    crear_usuario(
        username='mnavarro',
        tipo='Cliente', 
        nombre='Michael.', 
        apellido='Navarro', 
        correo=test_user_email if test_user_email else 'mnavarro@duocuc.cl', 
        es_superusuario=False, 
        es_staff=False, 
        rut='20723447-8',	
        direccion='303 Villa  Sur, Pedro Aguirre Cerda, \nSantiago 90001 \nChile', 
        subscrito=True, 
        imagen='perfiles/mnavarro.jpg'
    )

    crear_usuario(
        username='amunoz',
        tipo='Cliente', 
        nombre='Ana', 
        apellido='Munoz', 
        correo=test_user_email if test_user_email else 'a.munoz@duocuc.cl', 
        es_superusuario=False, 
        es_staff=False, 
        rut='18240323-7',	
        direccion='503 Maipu, El monte, \nSantiago 61000 \nChile', 
        subscrito=True, 
        imagen='perfiles/amunoz.jpg'
    )
    #----------

    crear_usuario(
        username='eperez',
        tipo='Cliente', 
        nombre='Evaristo', 
        apellido='Perez', 
        correo=test_user_email if test_user_email else 'eperez@duocuc.cl', 
        es_superusuario=False, 
        es_staff=False, 
        rut='25.747.200-0',	
        direccion='223 Las Condes, Providencia, \nSantiago 61000 \nChile', 
        subscrito=True, 
        imagen='perfiles/eperez.jpg')

    crear_usuario(
        username='mferrada',
        tipo='Cliente', 
        nombre='Matias', 
        apellido='Ferrada', 
        correo=test_user_email if test_user_email else 'm.ferrada@duocuc.cl', 
        es_superusuario=False, 
        es_staff=False, 
        rut='20.202.357-5', 
        direccion='Las Lilas, PAC, \nSantiago 10001 \nChile', 
        subscrito=True, 
        imagen='perfiles/mferrada.jpg')

    crear_usuario(
        username='ccontreras',
        tipo='Cliente', 
        nombre='Camilo', 
        apellido='Contreras', 
        correo=test_user_email if test_user_email else 'ccontreras@duocuc.cl', 
        es_superusuario=False, 
        es_staff=False, 
        rut='11.991.600-3', 
        direccion='San Jose de la Estrella, Puente Alto, \nSantiago, 95014 \nChile', 
        subscrito=False, 
        imagen='perfiles/ccontreras.jpg')

    crear_usuario(
        username='amontalva',
        tipo='Cliente', 
        nombre='Antonia', 
        apellido='Montalva', 
        correo=test_user_email if test_user_email else 'amontalva@duocuc.cl', 
        es_superusuario=False, 
        es_staff=False, 
        rut='16.469.725-8', 
        direccion='San Miguel 5th Avenida, \nSantiago, 10118 \nChile', 
        subscrito=False, 
        imagen='perfiles/amontalva.jpg')

    crear_usuario(
        username='rgonzalez',
        tipo='Administrador', 
        nombre='Rodrigro', 
        apellido='Gonzalez', 
        correo=test_user_email if test_user_email else 'rgonzalez@duocuc.cl', 
        es_superusuario=False, 
        es_staff=True, 
        rut='19.441.980-5', 
        direccion='San Felipe 5323, \nValparaiso 33101 \nChile', 
        subscrito=False, 
        imagen='perfiles/rgonzalez.jpg')
    
    crear_usuario(
        username='cmartinez',
        tipo='Administrador', 
        nombre='Cesar', 
        apellido='Martinez', 
        correo=test_user_email if test_user_email else 'cmartinez@duocuc.cl', 
        es_superusuario=False, 
        es_staff=True, 
        rut='21.708.052-3', 
        direccion='Peñaflor 5422, \nSantiago \nChile', 
        subscrito=False, 
        imagen='perfiles/cmartinez.jpg')

    crear_usuario(
        username='super',
        tipo='Superusuario',
        nombre='Sol',
        apellido='Martinez',
        correo=test_user_email if test_user_email else 'smartinez@duocuc.cl',
        es_superusuario=True,
        es_staff=True,
        rut='13.029.317-4',
        direccion='Peñaflor 5422, \nSantiago \nChile',
        subscrito=False,
        imagen='perfiles/smartinez.jpg')
    
    categorias_data = [
        { 'id': 1, 'nombre': 'Shooter'},
        { 'id': 2, 'nombre': 'Deportes'},
        { 'id': 3, 'nombre': 'Puzzle'},
        { 'id': 4, 'nombre': 'Simulación'},
    ]

    print('Crear categorías')
    for categoria in categorias_data:
        Categoria.objects.create(**categoria)
    print('Categorías creadas correctamente')

    productos_data = [
        # Categoría "Shooter" (5 juegos)
        {
            'id': 1,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Halo Infinite',
            'descripcion': 'Halo Infinite es un shooter en primera persona desarrollado por 343 Industries y publicado por Xbox Game Studios. Es la sexta entrega principal de la serie Halo y sigue al Jefe Maestro en su lucha contra la amenaza de los Banished en un mundo abierto.',
            'precio': 59990,
            'descuento_subscriptor': 10,
            'descuento_oferta': 20,
            'imagen': 'productos/000001_kBvdw39.jpg'
        },
        {
            'id': 2,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Overwatch 2',
            'descripcion': 'Overwatch 2 es un juego de disparos en equipo desarrollado y publicado por Blizzard Entertainment. El juego introduce nuevas misiones de historia cooperativa y modos de juego, así como nuevos héroes y mapas.',
            'precio': 49990,
            'descuento_subscriptor': 10,
            'descuento_oferta': 15,
            'imagen': 'productos/000002_zjg38GX.jpg'
        },
        {
            'id': 3,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Rainbow Six Siege',
            'descripcion': 'Tom Clancy\'s Rainbow Six Siege es un shooter táctico en primera persona desarrollado por Ubisoft Montreal y publicado por Ubisoft. Los jugadores controlan a los operadores de diferentes unidades antiterroristas en enfrentamientos multijugador.',
            'precio': 39990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 10,
            'imagen': 'productos/000003_DxwaCeS.jpg'
        },
        {
            'id': 4,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Battlefield 2042',
            'descripcion': 'Battlefield 2042 es un shooter en primera persona desarrollado por DICE y publicado por Electronic Arts. El juego está ambientado en un futuro cercano y presenta grandes batallas multijugador con hasta 128 jugadores en mapas dinámicos.',
            'precio': 69990,
            'descuento_subscriptor': 10,
            'descuento_oferta': 20,
            'imagen': 'productos/000004_F3QX7Fc.jpg'
        },
        {
            'id': 5,
            'categoria': Categoria.objects.get(id=1),
            'nombre': 'Valorant',
            'descripcion': 'Valorant es un shooter táctico en primera persona desarrollado y publicado por Riot Games. El juego combina elementos de disparos y habilidades únicas para cada personaje, ofreciendo un estilo de juego estratégico y competitivo.',
            'precio': 19990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 15,
            'imagen': 'productos/000005_ApSAbeS.jpg'
        },
        # Categoría "Deportes" (5 juegos)
        {
            'id': 6,
            'categoria': Categoria.objects.get(id=2),
            'nombre': 'FIFA 23',
            'descripcion': 'FIFA 23 es un videojuego de simulación de fútbol desarrollado y publicado por Electronic Arts. El juego presenta a los mejores equipos y jugadores de fútbol del mundo, ofreciendo modos de juego tanto en solitario como multijugador.',
            'precio': 59990,
            'descuento_subscriptor': 10,
            'descuento_oferta': 20,
            'imagen': 'productos/000006_wbhH394.jpg'
        },
        {
            'id': 7,
            'categoria': Categoria.objects.get(id=2),
            'nombre': 'NBA 2K23',
            'descripcion': 'NBA 2K23 es un videojuego de simulación de baloncesto desarrollado por Visual Concepts y publicado por 2K Sports. El juego ofrece una experiencia realista de la NBA, con modos de juego variados y una gran fidelidad gráfica.',
            'precio': 69990,
            'descuento_subscriptor': 10,
            'descuento_oferta': 20,
            'imagen': 'productos/000007_HugwH2Y.jpg'
        },
        {
            'id': 8,
            'categoria': Categoria.objects.get(id=2),
            'nombre': 'Madden NFL 23',
            'descripcion': 'Madden NFL 23 es un videojuego de simulación de fútbol americano desarrollado y publicado por Electronic Arts. El juego ofrece una experiencia auténtica de la NFL, con gráficos mejorados y modos de juego variados.',
            'precio': 49990,
            'descuento_subscriptor': 10,
            'descuento_oferta': 15,
            'imagen': 'productos/000008_WtJOBqZ.jpg'
        },
        {
            'id': 9,
            'categoria': Categoria.objects.get(id=2),
            'nombre': 'Tony Hawk\'s Pro Skater 1+2',
            'descripcion': 'Tony Hawk\'s Pro Skater 1+2 es un videojuego de skateboarding desarrollado por Vicarious Visions y publicado por Activision. El juego es una remasterización de los dos primeros juegos de la serie Tony Hawk\'s Pro Skater, ofreciendo gráficos mejorados y una jugabilidad clásica.',
            'precio': 39990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 10,
            'imagen': 'productos/000009_tL7J5cP.jpg'
        },
        {
            'id': 10,
            'categoria': Categoria.objects.get(id=2),
            'nombre': 'Gran Turismo 7',
            'descripcion': 'Gran Turismo 7 es un videojuego de carreras desarrollado por Polyphony Digital y publicado por Sony Interactive Entertainment. El juego ofrece una experiencia de conducción realista, con una gran variedad de coches y circuitos.',
            'precio': 69990,
            'descuento_subscriptor': 10,
            'descuento_oferta': 20,
            'imagen': 'productos/000010_qB7Kyt0.jpg'
        },
        # Categoría "Puzzle" (5 juegos)
        {
            'id': 11,
            'categoria': Categoria.objects.get(id=3),
            'nombre': 'Tetris Effect',
            'descripcion': 'Tetris Effect es un videojuego de rompecabezas desarrollado por Monstars y Resonair y publicado por Enhance Games. El juego ofrece una experiencia inmersiva de Tetris, con efectos visuales y sonoros sincronizados con la jugabilidad.',
            'precio': 29990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 15,
            'imagen': 'productos/000011_V3pdxE4.jpg'
        },
        {
            'id': 12,
            'categoria': Categoria.objects.get(id=3),
            'nombre': 'Portal 2',
            'descripcion': 'Portal 2 es un videojuego de rompecabezas en primera persona desarrollado y publicado por Valve Corporation. El juego sigue a Chell mientras usa el Portal Gun para resolver una serie de rompecabezas y escapar de las instalaciones de Aperture Science.',
            'precio': 19990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 10,
            'imagen': 'productos/000012_aD8XQ9t.jpg'
        },
        {
            'id': 13,
            'categoria': Categoria.objects.get(id=3),
            'nombre': 'The Witness',
            'descripcion': 'The Witness es un videojuego de rompecabezas en primera persona desarrollado y publicado por Jonathan Blow. El juego presenta un mundo abierto lleno de rompecabezas desafiantes que los jugadores deben resolver para descubrir la historia subyacente.',
            'precio': 39990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 15,
            'imagen': 'productos/000013_KZxVxa1.jpg'
        },
        {
            'id': 14,
            'categoria': Categoria.objects.get(id=3),
            'nombre': 'Baba Is You',
            'descripcion': 'Baba Is You es un videojuego de rompecabezas desarrollado por Hempuli. El juego permite a los jugadores cambiar las reglas del juego moviendo palabras en el entorno, creando nuevas interacciones y soluciones para los rompecabezas.',
            'precio': 19990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 10,
            'imagen': 'productos/000014_cOze7oQ.jpg'
        },
        {
            'id': 15,
            'categoria': Categoria.objects.get(id=3),
            'nombre': 'Human: Fall Flat',
            'descripcion': 'Human: Fall Flat es un videojuego de rompecabezas y plataformas desarrollado por No Brakes Games y publicado por Curve Digital. El juego presenta un personaje llamado Bob, que los jugadores deben controlar para resolver rompecabezas físicos en una serie de niveles.',
            'precio': 29990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 15,
            'imagen': 'productos/000015_vmLUsiW.jpg'
        },
        # Categoría "Simulación" (5 juegos)
        {
            'id': 16,
            'categoria': Categoria.objects.get(id=4),
            'nombre': 'The Sims 4',
            'descripcion': 'The Sims 4 es un videojuego de simulación de vida desarrollado por Maxis y publicado por Electronic Arts. Los jugadores pueden crear y controlar personas en un mundo virtual, construyendo casas y desarrollando relaciones.',
            'precio': 39990,
            'descuento_subscriptor': 10,
            'descuento_oferta': 20,
            'imagen': 'productos/000016_Xn6EHti.jpg'
        },
        {
            'id': 17,
            'categoria': Categoria.objects.get(id=4),
            'nombre': 'Flight Simulator',
            'descripcion': 'Microsoft Flight Simulator es un videojuego de simulación de vuelo desarrollado por Asobo Studio y publicado por Xbox Game Studios. El juego ofrece una simulación realista de vuelo, con gráficos de alta calidad y una recreación detallada del mundo.',
            'precio': 99990,
            'descuento_subscriptor': 15,
            'descuento_oferta': 25,
            'imagen': 'productos/000017_VgAJneE.jpg'
        },
        {
            'id': 18,
            'categoria': Categoria.objects.get(id=4),
            'nombre': 'Cities: Skylines',
            'descripcion': 'Cities: Skylines es un videojuego de simulación de construcción de ciudades desarrollado por Colossal Order y publicado por Paradox Interactive. Los jugadores pueden planificar y construir una ciudad, gestionando aspectos como la infraestructura, los servicios y la economía.',
            'precio': 29990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 15,
            'imagen': 'productos/000018_F5CUjiM.jpg'
        },
        {
            'id': 19,
            'categoria': Categoria.objects.get(id=4),
            'nombre': 'Stardew Valley',
            'descripcion': 'Stardew Valley es un videojuego de simulación de granja desarrollado por ConcernedApe. Los jugadores pueden cultivar, criar animales, pescar, minar y socializar con los habitantes del pueblo.',
            'precio': 19990,
            'descuento_subscriptor': 5,
            'descuento_oferta': 10,
            'imagen': 'productos/000019_6OuR7ee.jpg'
        },
        {
            'id': 20,
            'categoria': Categoria.objects.get(id=4),
            'nombre': 'Planet Zoo',
            'descripcion': 'Planet Zoo es un videojuego de simulación de construcción de zoológicos desarrollado y publicado por Frontier Developments. Los jugadores pueden construir y gestionar un zoológico, cuidando a los animales y creando hábitats realistas.',
            'precio': 49990,
            'descuento_subscriptor': 10,
            'descuento_oferta': 20,
            'imagen': 'productos/000020_9SLe8r4.jpg'
        }
    ]

    print('Crear productos')
    for producto in productos_data:
        Producto.objects.create(**producto)
    print('Productos creados correctamente')

    print('Crear carritos')
    for rut in ['25.747.200-0', '11.991.600-3']:
        cliente = Perfil.objects.get(rut=rut)
        for cantidad_productos in range(1, 11):
            producto = Producto.objects.get(pk=randint(1, 10))
            if cliente.subscrito:
                descuento_subscriptor = producto.descuento_subscriptor
            else:
                descuento_subscriptor = 0
            descuento_oferta = producto.descuento_oferta
            descuento_total = descuento_subscriptor + descuento_oferta
            descuentos = int(round(producto.precio * descuento_total / 100))
            precio_a_pagar = producto.precio - descuentos
            Carrito.objects.create(
                cliente=cliente,
                producto=producto,
                precio=producto.precio,
                descuento_subscriptor=descuento_subscriptor,
                descuento_oferta=descuento_oferta,
                descuento_total=descuento_total,
                descuentos=descuentos,
                precio_a_pagar=precio_a_pagar
            )
    print('Carritos creados correctamente')

    print('Crear boletas')
    nro_boleta = 0
    perfiles_cliente = Perfil.objects.filter(tipo_usuario='Cliente')
    for cliente in perfiles_cliente:
        estado_index = -1
        for cant_boletas in range(1, randint(6, 21)):
            nro_boleta += 1
            estado_index += 1
            if estado_index > 3:
                estado_index = 0
            estado = Boleta.ESTADO_CHOICES[estado_index][1]
            fecha_venta = date(2023, randint(1, 5), randint(1, 28))
            fecha_despacho = fecha_venta + timedelta(days=randint(0, 3))
            fecha_entrega = fecha_despacho + timedelta(days=randint(0, 3))
            if estado == 'Anulado':
                fecha_despacho = None
                fecha_entrega = None
            elif estado == 'Vendido':
                fecha_despacho = None
                fecha_entrega = None
            elif estado == 'Despachado':
                fecha_entrega = None
            boleta = Boleta.objects.create(
                nro_boleta=nro_boleta, 
                cliente=cliente,
                monto_sin_iva=0,
                iva=0,
                total_a_pagar=0,
                fecha_venta=fecha_venta,
                fecha_despacho=fecha_despacho,
                fecha_entrega=fecha_entrega,
                estado=estado)
            detalle_boleta = []
            total_a_pagar = 0
            for cant_productos in range(1, randint(4, 6)):
                producto_id = randint(1, 10)
                producto = Producto.objects.get(id=producto_id)
                precio = producto.precio
                descuento_subscriptor = 0
                if cliente.subscrito:
                    descuento_subscriptor = producto.descuento_subscriptor
                descuento_oferta = producto.descuento_oferta
                descuento_total = descuento_subscriptor + descuento_oferta
                descuentos = int(round(precio * descuento_total / 100))
                precio_a_pagar = precio - descuentos
                bodega = Bodega.objects.create(producto=producto)
                DetalleBoleta.objects.create(
                    boleta=boleta,
                    bodega=bodega,
                    precio=precio,
                    descuento_subscriptor=descuento_subscriptor,
                    descuento_oferta=descuento_oferta,
                    descuento_total=descuento_total,
                    descuentos=descuentos,
                    precio_a_pagar=precio_a_pagar)
                total_a_pagar += precio_a_pagar
            monto_sin_iva = int(round(total_a_pagar / 1.19))
            iva = total_a_pagar - monto_sin_iva
            boleta.monto_sin_iva = monto_sin_iva
            boleta.iva = iva
            boleta.total_a_pagar = total_a_pagar
            boleta.fecha_venta = fecha_venta
            boleta.fecha_despacho = fecha_despacho
            boleta.fecha_entrega = fecha_entrega
            boleta.estado = estado
            boleta.save()
            print(f'    Creada boleta Nro={nro_boleta} Cliente={cliente.usuario.first_name} {cliente.usuario.last_name}')
    print('Boletas creadas correctamente')

    print('Agregar productos a bodega')
    for producto_id in range(1, 11):
        producto = Producto.objects.get(id=producto_id)
        cantidad = 0
        for cantidad in range(1, randint(2, 31)):
            Bodega.objects.create(producto=producto)
        print(f'    Agregados {cantidad} "{producto.nombre}" a la bodega')
    print('Productos agregados a bodega')

