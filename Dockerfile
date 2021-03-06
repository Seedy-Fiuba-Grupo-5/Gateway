# Dockerfile para produccion

# Imagen base de python
FROM python:3.8

# Directorio de trabajo
WORKDIR /usr/src/app

# Actualizar repositorios de apt
RUN apt-get update

# Instalar dependencias
RUN pip install --upgrade pip
COPY ./requirements-prod.txt /usr/src/app/requirements-prod.txt
RUN pip install -Ur requirements-prod.txt

# Indica al inteprete de Python que no genere archivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1

# Indica a Python que su salida estandar se envie directamente
# a la terminal, sin esperar en un buffer intermedio.
ENV PYTHONUNBUFFERED 1

# Indica a Flask que estamos en un ambiente de produccion
ENV FLASK_ENV=production

# Indica a Flask en que modulo se encuetra la aplicacion
ENV FLASK_APP=./prod/manage

# Copiar archivos de produccion
COPY ./prod /usr/src/app/prod

# Ejecutar el script entrypoint.sh
ENTRYPOINT ["sh", "/usr/src/app/prod/entrypoint.sh"]
