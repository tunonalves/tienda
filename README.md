# Tienda — proyecto final Python/Django

Proyecto Final de Coder House 2022 del curso Python-Django.

Alumno: **Federico Tuñon Alves**.

Sitio del autor: <https://tunonalves.wixsite.com/federico>

Aplicación educativa con catálogo de productos, carrito basado en sesiones, servicios, blog, autenticación y formulario de contacto. Incluye una sección de cotizaciones que consulta un servicio externo. No debe considerarse una tienda lista para producción ni un flujo de compra completo.

## Estructura y funcionalidades

| Ruta | Responsabilidad |
| --- | --- |
| [manage.py](manage.py) | Entrada para los comandos administrativos de Django. |
| [ProyectoWeb/](ProyectoWeb/) | Configuración del proyecto, rutas principales y WSGI. |
| [ProyectoWebApp/](ProyectoWebApp/) | Página de inicio, plantilla base y recursos estáticos. |
| [tienda/](tienda/) | Categorías y productos con precio, imagen y disponibilidad. |
| [carro/](carro/) | Agregar, restar, eliminar y limpiar productos de la sesión. |
| [autenticacion/](autenticacion/) | Registro, ingreso, cierre de sesión y vistas de usuarios. |
| [blog/](blog/) y [servicios/](servicios/) | Publicaciones, categorías y servicios. |
| [pedidos/](pedidos/) | Modelos de pedidos y líneas; el procesamiento está incompleto. |
| [contacto/](contacto/) | Formulario con envío de correo. |
| [dolar/](dolar/) | Consultas HTTP de cotizaciones mediante `requests`. |
| [media/](media/) | Archivos multimedia incluidos en el repositorio. |

La configuración utiliza SQLite (`db.sqlite3`), plantillas de Django y `crispy_forms` con el paquete de plantillas `bootstrap4`. Los recursos estáticos incluyen Bootstrap, jQuery y Font Awesome.

## Requisitos y límite de reproducibilidad

Se necesita Python 3 y un entorno virtual. **No hay `requirements.txt`, `pyproject.toml` ni archivo de bloqueo de dependencias**, por lo que no se puede afirmar una combinación exacta de versiones compatible a partir del repositorio.

Dependencias identificadas en el código y la configuración:

| Paquete | Evidencia / uso |
| --- | --- |
| Django | Proyecto, modelos, formularios y autenticación. |
| django-crispy-forms | Aplicación `crispy_forms` y renderizado de formularios. |
| Pillow | Soporte de los campos `ImageField` de los modelos. |
| requests | Importación y consultas en `dolar/views.py`. |

Antes de iniciar, seleccionar y fijar versiones compatibles en un entorno aislado. La integración de crispy forms debe proporcionar las plantillas `bootstrap4`; no asumir que instalar las últimas versiones reproduce la configuración histórica. La lista anterior es una guía derivada del código, no un entorno probado.

## Preparación local

```bash
git clone git@github.com:tunonalves/tienda.git
cd tienda
python3 -m venv .venv
source .venv/bin/activate
```

En Windows, activar el entorno con `.venv\Scripts\Activate.ps1` desde PowerShell. Instalar las dependencias compatibles identificadas arriba antes de continuar.

Revisar localmente `ProyectoWeb/settings.py`: claves, base de datos, correo, `DEBUG` y hosts permitidos. No reutilizar secretos ni publicar valores privados. No hay un cargador de `.env` documentado aquí: crear ese archivo por sí solo no configura Django.

El repositorio incluye una base SQLite. No usar sus cuentas o datos como credenciales de prueba; hacer una copia de respaldo fuera del repositorio y configurar una base local nueva antes de migrar. Para evitar envíos reales durante pruebas de contacto, usar el backend de correo de consola de Django en la configuración local:

```python
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

Con las dependencias y la configuración local listas, los comandos habituales desde la raíz son:

```bash
python manage.py check
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 127.0.0.1:8000
```

`migrate` y `createsuperuser` escriben en la base configurada. Usar únicamente una base de desarrollo. Abrir <http://127.0.0.1:8000/>; el panel administrativo está en `/admin/`. No hay un conjunto de datos iniciales reproducible documentado: los registros se pueden crear en el administrador local.

### Rutas principales

Las rutas se registran en [ProyectoWeb/urls.py](ProyectoWeb/urls.py): `/servicios/`, `/blog/`, `/contacto/`, `/tienda/`, `/carro/`, `/pedidos/` y `/dolar/`. El registro está en `/autenticacion/` y el ingreso en `/autenticacion/loguear`.

## Limitaciones observables

- `pedidos/urls.py` solo expone la página de pedidos; no conecta `procesar_pedido`. Esa función llama a `enviar_mail` sin definición/importación y usa atributos de solicitud que necesitan revisión. No se documenta como un checkout operativo.
- `dolar/views.py` depende de una API externa en Heroku y no define tiempos de espera ni manejo de errores de red. No se comprobó la disponibilidad del servicio; visitar esa sección puede generar solicitudes externas.
- El formulario de contacto tiene destinatarios definidos en el código y realiza envíos de correo. No probarlo contra un servidor de correo real sin revisar esos destinatarios y la configuración.
- La vista `UserList` referencia `auth/listUser.html`, mientras que el archivo incluido es `auth/user_list.html`; esa pantalla requiere revisión.
- La configuración de desarrollo y las vistas que modifican datos requieren revisión de seguridad y permisos antes de cualquier exposición pública.

## Pruebas y verificación

Una vez preparado un entorno compatible, Django permite ejecutar:

```bash
python manage.py test
```

Existen módulos `tests.py` de plantilla; su presencia no demuestra cobertura funcional. También se conserva el documento original [Unit test.pdf](unit%20test/Unit%20test.pdf).

Esta revisión comprobó estáticamente rutas, modelos, vistas y configuración no secreta. No se instalaron dependencias, iniciaron servidores, ejecutaron migraciones o pruebas de Django, ni se consultaron la API de cotizaciones o servicios de correo. Los pasos de ejecución anteriores quedan pendientes de validación en un entorno local compatible.