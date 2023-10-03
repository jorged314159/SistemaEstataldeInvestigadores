# Sistema Estatal de Investigadores

Este repositorio contiene el proyecto del SEI el cual debera ir en el dominio https://secyt.cozcyt.gob.mx/SDHJKssd283764/usuarios/login

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos Windows o Linux 🖥🐧️📋

```
Docker V24.0.6  superior
Docker Compose V2.15.1 o suprior
```

### Instalación 🔧

_Clonar el repositorio en una ruta de facil acceso con el siguiente comando:_

```console
root@pc:~$ git clone https://labsol.cozcyt.gob.mx/gitlab/devops-lab/sistema-estatal-de-investigadores.git
```

_Una vez descargado ingresaremos a la carpeta del proyecto con:_

```console
root@pc:~$ cd sistema-estatal-de-investigadores
```

_Dentro de la carpeta del proyecto haremos un:_

```console
root@pc:~$ docker compose up -d
```

_Este comando realizara la instalación de todas las dependencias necesarias para el fincionamiento del proyecto._

_Una vez terminado este proceso podremos ver los nuevos contenedores con el comando:_
```console
root@pc:~$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED       STATUS         PORTS                            NAMES
95389a82be47   sei-app   "fish"                   8 weeks ago   Up 6 seconds   80/tcp, 0.0.0.0:8000->8000/tcp   curso
b0de61d29f76   mariadb   "docker-entrypoint.s…"   8 weeks ago   Up 6 seconds   0.0.0.0:3310->3306/tcp           db-vinculacion
```


## Despliegue 📦

_Para hacer deploy a nuestro proyecto debemos entrar al contenedor de la aplicación y ejecutar los siguientes comandos:_
```console
root@pc:~$ docker exec -it CONTAINER_ID bash
root@CONTAINER_ID:/app# python3 manage.py makemigrations
root@CONTAINER_ID:/app# python3 manage.py migrate
root@CONTAINER_ID:/app# mkdir -p media/ZIPs
root@CONTAINER_ID:/app# mkdir -p media/Constancias/Word
root@CONTAINER_ID:/app# python3 manage.py runserver 0:8000
```
_Y tendremos nuestra aplicación funcionando a la perfeccion:_

## Construido con 🛠

* [Docker](https://www.docker.com/) - Programa para desarrollo y despliegue.
* [Django](https://www.djangoproject.com/) - Framework de desarrollo.
* [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) - Usado para los estilos de las vistas.

## Autores ✒️

* **Juventino Aguilar Correo.** - *Trabajo Inicial*
* **Elías Emiliano Beltrán González** - *Trabajo Inicial*
* **Román Guzmán Valles** - *Trabajo Inicial*

## Licencia 📄

Este proyecto está bajo la Licencia (GPL3.0) - mira el archivo [LICENSE.md](https://labsol.cozcyt.gob.mx/gitlab/devops-lab/sistema-estatal-de-investigadores/-/blob/main/LICENSE) para más detalles.

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* etc.
