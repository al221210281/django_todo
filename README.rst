Lista de Pendientes
===================

Lista de Pendientes

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


Instalación
-----------

Docker
^^^^^^

Generar el ambiente de desarrollo con docker build::

    $ docker-compose -f local.yml build

Ejecutar los contenedores configurados::

    $ docker-compose -f local.yml up

Usar la opción -d para mandar los procesos a segundo plano.

Crear el administrador del sistema::

    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser
