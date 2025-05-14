# Usa una imagen oficial de Python
FROM python:3.12-slim

# Instala dependencias del sistema necesarias para EFS y Flask
RUN apt-get update && apt-get install -y nfs-common && apt-get clean

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos al contenedor
COPY . .
COPY .env .env
ENV $(cat .env | xargs)

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Crea el directorio para EFS
RUN mkdir -p /mnt/efs

# Expone el puerto 80 para Flask
EXPOSE 80

# Comando para correr la app
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
