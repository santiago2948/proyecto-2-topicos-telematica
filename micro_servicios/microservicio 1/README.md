para iniciar la base de datos y crear las tablas:

flask shell
>>> from extensions import db
>>> db.create_all()
    sudo docker build --force-rm -t pythonMonolitic/latest . --no-cache
    sudo docker run -d --restart always   -e HOST_IP=<ip_privada_host>   -p 5000:5000   --name monolitic-server   pythonMonolitic/latest:latest