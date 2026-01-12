cd crud_m

# 2. Ejecutar UN SOLO comando:
docker run -d -p 8000:8000 --name django-django crud_m

si hay contenedores en uso probar docker run -d -p 8001:8000 --name django-app crud_m
# 3. Abrir en navegador:
# http://localhost:8000

# problemas de permiso activar 
docker run -d -p 8000:8000 --name django-django crud_m
sudo usermod -aG docker $USER
newgrp docker
