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

### Objetivo 2: Escalamiento Monolito

- **Autoescalamiento**: Configurar grupo de autoescalado en AWS.
- **ELB**: Balanceador de carga para distribuir tráfico.
- **Base de datos**: RDS MySQL o cluster de alta disponibilidad.
- **NFS**: Servidor NFS para archivos compartidos.

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
