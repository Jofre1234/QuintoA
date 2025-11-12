# imagen base
FROM python:3.12-slim

# crear directorion de trabajo
WORKDIR /app

# Copiar el archivo de la aplicación
COPY app.py /app

# Instalar dependencias
RUN pip install --no-cache-dir Flask

# Exponer el puerto 80
EXPOSE 80

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
