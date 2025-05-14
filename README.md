# ST0263-7290

# Estudiante(s):
- Daniel Correa Botero, dcorreab2@eafit.edu.co
- Miguel Ángel Cano Salinas, macanos1@eafit.edu.co
- Santiago Acevedo Urrego, sacevedou1@eafit.edu.co

# Profesor:
- Edwin Montoya, emontoya@eafit.edu.co

# Proyecto: BookStore - Sistema Distribuido de Venta de Libros de Segunda

## 1. Breve descripción de la actividad

BookStore es una aplicación que simula un sistema de ecommerce para la venta de libros de segunda mano, donde los usuarios pueden publicar, comprar y vender libros. A diferencia de las apps de tiendas que conocemos, BookStore permite a los usuarios gestionar su propio inventario y publicar libros para la venta.

Actualmente, BookStore permite:
- Autenticación de usuarios (registro, login, logout)
- Visualización del catálogo de libros publicados
- Compra de libros (gestión de stock)
- Pago simulado
- Envío simulado de libros

El proyecto se desarrolla en tres objetivos principales:

### Objetivo 1: Despliegue Monolítico en AWS (20%)
Desplegar la aplicación BookStore monolítica en una VM en AWS, con dominio propio, certificado SSL y proxy inverso en NGINX.

### Objetivo 2: Escalamiento Monolítico en AWS (30%)
Escalar la aplicación monolítica utilizando VMs con autoescalamiento, base de datos administrada o con alta disponibilidad, y archivos compartidos vía NFS. Se debe utilizar un balanceador de carga administrado (ELB) y mantener el dominio y certificado.

### Objetivo 3: Reingeniería a Microservicios y Orquestación con Docker Swarm (50%)
Utilizar la aplicación monolítica y hacer el despliegue respectivo en un cluster de contenedores (Docker Swarm), dado que el EKS no está disponible en AWS Academy

---

## 2. Diseño de alto nivel, arquitectura, patrones y mejores prácticas

### Arquitectura

- **Monolito**: Python Flask + MySQL, articulados con docker-compose.
- **Microservicios**: Tres servicios independientes (Autenticación, Catálogo, Compra/Pago/Entrega), cada uno con su propia base de datos.
- **Balanceador de carga**: ELB para escalamiento
- **Almacenamiento compartido**: NFS para archivos.
- **Orquestación**: Docker Swarm para microservicios.


### Patrones de disponibilidad y rendimiento

- **Balanceo de carga**: ELB/NGINX distribuye tráfico entre instancias.
- **Redundancia y autoescalamiento**: VMs con autoescalado y alta disponibilidad.
- **Separación de responsabilidades**: Cada microservicio tiene una función clara.
- **Persistencia y consistencia**: Uso de bases de datos administradas o replicadas.
- **CQRS (en microservicios)**: Separación de lectura y escritura en bases de datos para catálogo y operaciones.

### Mejores prácticas

- Uso de variables de entorno para configuración.
- Certificados SSL y dominio propio.
- Despliegue automatizado con Docker y Docker Compose/Swarm.
- Documentación y scripts de despliegue reproducibles.

---

## 3. Ambiente local para desarrollo

### Requisitos

- Python 3.10+
- Docker y Docker Compose
- MySQL 8+

### Instalación y ejecución (Monolito)

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/santiago2948/proyecto-2-topicos-telematica
    cd proyecto-2-topicos-telematica/
    ```

2. Configurar variables de entorno en `.env` (ver ejemplo en `.env.example`).

3. Levantar la aplicación y la base de datos:
    ```bash
    docker-compose up --build
    ```

4. Acceder a la aplicación en [http://localhost](http://localhost).

### Estructura de archivos (Monolito)

```
├── app/
│   ├── main.py
│   ├── models/
│   ├── routes/
│   ├── templates/
│   └── static/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 4. Despliegue en producción

### Objetivo 1: Monolito en AWS

- **VM**: Ubuntu 22.04 en AWS EC2
- **Dominio y SSL**: Configurar dominio propio y Let's Encrypt
- **NGINX**: Proxy inverso y terminación SSL

#### Pasos principales

1. Crear VM en AWS y asociar dominio.
2. Instalar Docker, Docker Compose y NGINX.
3. Configurar certificados SSL.
4. Desplegar la app con Docker Compose.
5. Configurar NGINX como proxy inverso.

#### Comandos para desplegar el monolito en AWS

1. **Actualizar e instalar dependencias básicas**
    ```bash
    sudo apt-get update && sudo apt-get upgrade -y
    sudo apt-get install -y git curl
    ```

2. **Instalar Docker y Docker Compose**
    ```bash
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker $USER
    # Cierra sesión y vuelve a entrar para aplicar el grupo docker

    # Instalar Docker Compose
    sudo apt-get install -y docker-compose
    ```

3. **Clonar el repositorio y posicionarse en la carpeta del monolito**
    ```bash
    git clone https://github.com/santiago2948/proyecto-2-topicos-telematica.git
    cd proyecto-2-topicos-telematica/objetivo3/monolito
    ```

4. **Configurar variables de entorno**
    ```bash
    cp .env.example .env
    # Edita .env con tus valores de producción
    nano .env
    ```

5. **Levantar la aplicación con Docker Compose**
    ```bash
    sudo docker-compose up --build -d
    ```

6. **Instalar NGINX**
    ```bash
    sudo apt-get install -y nginx
    ```

7. **Configurar NGINX como proxy inverso**
    - Crea un archivo de configuración, por ejemplo `/etc/nginx/sites-available/bookstore`:
      ```
      server {
          listen 80;
          server_name TU_DOMINIO;

          location / {
              proxy_pass http://localhost:80;
              proxy_set_header Host $host;
              proxy_set_header X-Real-IP $remote_addr;
              proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
              proxy_set_header X-Forwarded-Proto $scheme;
          }
      }
      ```
    - Habilita el sitio y recarga NGINX:
      ```bash
      sudo ln -s /etc/nginx/sites-available/bookstore /etc/nginx/sites-enabled/
      sudo nginx -t
      sudo systemctl reload nginx
      ```

8. **Instalar Certbot y obtener certificado SSL**
    ```bash
    sudo apt-get install -y certbot python3-certbot-nginx
    sudo certbot --nginx -d https://telematica-libros.shop/
    ```

9. **Verifica que todo esté funcionando**
    - Accede a `https:https://telematica-libros.shop/` en tu navegador.

---

### Objetivo 2: Escalamiento Monolito

- **Autoescalamiento**: Configurar grupo de autoescalado en AWS.
- **ELB**: Balanceador de carga para distribuir tráfico.
- **Base de datos**: RDS MySQL o cluster de alta disponibilidad.
- **NFS**: Servidor NFS para archivos compartidos.

#### Pasos para desplegar el monolito escalable en AWS

1. **Crear un grupo de Auto Scaling (ASG)**
    - Ve a EC2 > Auto Scaling Groups > Create Auto Scaling group.
    - Elige un *Launch Template* o *Launch Configuration* con:
        - **AMI**: Ubuntu 22.04
        - **Tipo de instancia**: t3.small (o similar)
        - **User Data**:  
          _Pega aquí tu script de user data para instalar Docker, Docker Compose, montar EFS, clonar el repo y levantar el contenedor._
          ```
          #!/bin/bash

# Actualiza el sistema
sudo apt update -y
sudo apt upgrade -y

# Instala Docker, Docker Compose y utilidades para EFS
sudo apt install -y docker.io docker-compose nfs-common

# Activa e inicia Docker
sudo systemctl enable docker
sudo systemctl start docker

# Crea el punto de montaje para el EFS
sudo mkdir -p /mnt/efs

# Monta el EFS
sudo mount -t nfs4 -o nfsvers=4.1 fs-015fb9d53f7395e8d.efs.us-east-1.amazonaws.com:/ /mnt/efs

# Verifica que el EFS esté montado
df -h | grep efs

# Clona el repositorio de la app
git clone https://github.com/santiago2948/proyecto-2-topicos-telematica.git
cd proyecto-2-topicos-telematica/objetivo2/monolito

# Construye y ejecuta el contenedor
sudo docker build --force-rm -t pythonMonolitic/latest . --no-cache
sudo docker run -d --restart always -p 80:80 --name monolitic-server \
-e DB_HOST=database-objective-2.c9wuu22ec2ri.us-east-1.rds.amazonaws.com \
-e DB_USER=admin \
-e DB_PASS=Salinitrato10. \
-e DB_NAME=bookstore \
-v /mnt/efs:/mnt/efs pythonMonolitic/latest
          ```
        - **Security Groups**: Permitir puertos 80, 443, y acceso a EFS y RDS.
    - Configura el grupo con:
        - **Mínimo**: 2 instancias
        - **Máximo**: 5 instancias
        - **Deseado**: 2 instancias
    - Adjunta el grupo al Target Group del Load Balancer.

2. **Crear un Load Balancer (ELB)**
    - Ve a EC2 > Load Balancers > Create Application Load Balancer.
    - Configura listeners en **HTTP (80)** y **HTTPS (443)**.
    - Asocia el Target Group creado para el ASG.
    - Configura el Security Group para permitir tráfico web.

3. **Crear la base de datos RDS (MySQL)**
    - Ve a RDS > Create database.
    - Elige MySQL, instancia db.t3.micro, almacenamiento y credenciales.
    - Permite acceso desde el Security Group de las instancias EC2.
    - Anota el endpoint, usuario y contraseña para el archivo `.env`.

4. **Crear y montar EFS**
    - Ve a EFS > Create file system.
    - Configura el Security Group para permitir NFS (2049) desde las instancias EC2.
    - Monta EFS en `/mnt/efs` en cada instancia (esto debe estar en el user data).

5. **Configurar CNAME en tu dominio**
    - En tu proveedor de dominio, crea un registro CNAME apuntando a la DNS del Load Balancer.

6. **Solicitar y asociar certificado SSL en el Load Balancer**
    - Ve a AWS Certificate Manager (ACM) > Request certificate.
    - Solicita un certificado para tu dominio (ej: `telematica-libros.shop`).
    - Valida el dominio (por DNS o email).
    - En el Load Balancer, edita el listener HTTPS (443) y asocia el certificado de ACM.

7. **Configurar variables de entorno y conexión en Docker Compose**
    - En `objetivo2/monolito/.env`:
      ```
      SECRET_KEY=suprsecreto
      DB_USER=admin
      DB_PASS=12345678
      DB_HOST=<endpoint_RDS>
      DB_NAME=bookstore
      ```
    - En `docker-compose.yml`, asegúrate de montar EFS:
      ```yaml
      volumes:
        - /mnt/efs:/mnt/efs
      ```

8. **Desplegar la aplicación en cada instancia (esto debe estar en el user data)**
    - Clonar el repo, copiar `.env`, y levantar con Docker Compose:
      ```bash
      git clone https://github.com/santiago2948/proyecto-2-topicos-telematica.git
      cd proyecto-2-topicos-telematica/objetivo2/monolito
      cp /ruta/.env .env
      sudo docker-compose up --build -d
      ```

---

### Objetivo 3: Microservicios con Docker Swarm

- **División en microservicios**: Autenticación, Catálogo, Compra/Pago/Entrega.
- **Orquestación**: Docker Swarm para despliegue y escalabilidad.
- **Persistencia**: Bases de datos independientes o compartidas según etapa.
- **Balanceo**: Swarm y NGINX/ELB.

---

## 5. Configuración de parámetros

- **Variables de entorno**: `.env` para configuración de base de datos, puertos, claves secretas, etc.
- **Conexión a base de datos**: Configurada en variables de entorno y archivos de configuración.
- **Puertos**: Definidos en `docker-compose.yml` y archivos de configuración.
- **Certificados SSL**: Ubicados en `/etc/letsencrypt/` o ruta definida en NGINX.

---

## 7. Referencias

- [Docker Docs](https://docs.docker.com/)
- [Docker Compose Docs](https://docs.docker.com/compose/)
- [Docker Swarm Docs](https://docs.docker.com/engine/swarm/)
- [NGINX Docs](https://nginx.org/en/docs/)
- [AWS EC2 Docs](https://docs.aws.amazon.com/ec2/)
- [AWS RDS Docs](https://docs.aws.amazon.com/rds/)
- [Let's Encrypt Docs](https://letsencrypt.org/docs/)
- [CQRS Pattern](https://martinfowler.com/bliki/CQRS.html)
