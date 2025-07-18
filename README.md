# EMS - Employee Management System

Este proyecto es una aplicación web desarrollada con Django para gestionar empleados y sus trabajos.

## Requisitos

- Python 3.8+
- pip
- Virtualenv (opcional, pero recomendado)

## Instalación

1. **Clona el repositorio**  
   ```sh
   git clone <URL_DEL_REPOSITORIO>
   cd ems_django
   ```

2. **Crea y activa un entorno virtual**  
   ```sh
   python -m venv env
   # En Windows:
   env\Scripts\activate
   # En Mac/Linux:
   source env/bin/activate
   ```

3. **Instala las dependencias**  
   ```sh
   pip install -r requirements.txt
   ```

4. **Aplica las migraciones**  
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crea un superusuario (opcional, para acceder al admin)**  
   ```sh
   python manage.py createsuperuser
   ```

6. **Inicia el servidor de desarrollo**  
   ```sh
   python manage.py runserver
   ```

7. **Accede a la aplicación**  
   Abre tu navegador en [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Estructura del Proyecto

- `ems/`  
  Contiene la aplicación principal, modelos, vistas y plantillas.
- `ems_site/`  
  Configuración global del proyecto Django.
- `templates/ems/`  
  Plantillas HTML para la interfaz de usuario.

## Funcionalidades

- Listado de empleados con sus datos y trabajos asociados.
- Vista de detalle para cada empleado.
- Panel de administración para gestionar empleados y trabajos.

## Configuración adicional

- El idioma y la zona horaria están configurados para Argentina en [`ems_site/settings.py`](ems_site/settings.py).
- La base de datos por defecto es SQLite (`db.sqlite3`).

## Personalización

Puedes modificar los modelos en [`ems/models.py`](ems/models.py) y las vistas en [`ems/views.py`](ems/views.py) para adaptar la aplicación a tus necesidades.

---