# Usa una imagen base de Python
FROM python:3.8-alpine

# Instala las herramientas de compilación de C y las dependencias de desarrollo
RUN apk add --no-cache gcc musl-dev

# Establece la variable de entorno PYTHONUNBUFFERED en 1 para evitar problemas con la salida de la consola
ENV PYTHONUNBUFFERED=1

# Establece el directorio de trabajo en /code
WORKDIR /code

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias usando pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia el resto del código al directorio de trabajo
COPY . .

# Expone el puerto 8000 para acceder a la aplicación Django
EXPOSE 8000

# Comando para ejecutar la aplicación Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
