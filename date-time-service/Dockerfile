# Usar una imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requisitos al contenedor
COPY requirements.txt /app/

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código al contenedor
COPY . /app/

# Exponer el puerto en el que Flask estará corriendo
EXPOSE 5001

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
