# Usa una imagen base oficial de Python 3.
FROM python:3.9-slim

# Configura el directorio de trabajo dentro del contenedor.
WORKDIR /app

# Variables de entorno.
# ENV PYTHONUNBUFFERED=true
ENV VAR_NAME=var_value

# Copia e instala los requisitos de dependencia.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos del proyecto en el contenedor.
COPY . .

# Expone el puerto en el que se ejecuta tu aplicación.
EXPOSE 8000

# Define el comando para ejecutar tu aplicación.
# REVISAR SI ESTE CMD ES CORRECTO PARA MI PROYECTO DE DJANGO.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mysite.wsgi"]
