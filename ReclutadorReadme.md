cd crud_m

# Método uno 
# Ejecutar UN SOLO comando:
docker run -d -p 8000:8000 --name django-django crud_m
si hay contenedores en uso probar docker run -d -p 8001:8000 --name django-app crud_m

# 3. Abrir en navegador,o según el puerto elegido:
# http://localhost:8000

# Si surge problemas con permiso de usuario

sudo usermod -aG docker $USER
newgrp docker
docker run -d -p 8000:8000 --name django-django crud_m