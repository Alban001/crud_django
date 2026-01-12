# Cambia python:3.11-slim por python:3.12-slim
FROM python:3.12-slim

WORKDIR /app

# Instalar dependencias del sistema (si es necesario)
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar proyecto
COPY . .

# Puerto
EXPOSE 8000

# Comando para ejecutar
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]