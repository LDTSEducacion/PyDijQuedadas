# Proyecto de Gestión de Quedadas

Este es un proyecto de Django para gestionar quedadas entre usuarios.

## Configuración del Entorno

1. Instalación de Python:
   - Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/).

2. Clonar el Repositorio:

3. Instalación de Dependencias:
   Navega hasta el directorio del proyecto y ejecuta:
   pip install -r requirements.txt

4. Configuración de la Base de Datos:
  Asegúrate de tener PostgreSQL instalado y configurado
  Edita la configuración de la base de datos en proyecto_quedadas/settings.py

5 Aplicar Migraciones:
  python manage.py makemigrations
  python manage.py migrate
  
6. Ejecutar el Proyecto
  python manage.py runserver

7. Acceder al Sitio:
  Abre tu navegador y visita http://localhost:8000

9. Crear un Superusuario
  Ejecutar el Comando:
  python manage.py createsuperuser
  Sigue las instrucciones para crear un superusuario

Funcionalidades:
- CRUD de usuarios: Gestiona los usuarios del sistema
- CRUD de quedadas: Gestiona las quedadas entre usuarios
- Listar usuarios: lista todos los usuarios creados
- Listar quedadas: lista todos los quedadas creadas
- Eliminar usuarios: elimina el usuario seleccionado por su id
- Eliminar quedadas: elimina el quedadas seleccionada por su id
