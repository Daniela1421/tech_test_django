# 🧾 Prueba Técnica Backend - Registro de Usuarios e Ingresos

Este proyecto es una API desarrollada con Django y Django REST Framework, creada como parte de una prueba técnica.

## 🚀 Requisitos

- Python 3.10+
- Docker ≥ 20.10
- Docker Compose ≥ 1.29

## 🔧 Instalación y ejecución

### 1. Clona este repositorio

```bash
git clone https://github.com/Daniela1421/tech_test_django.git
cd tech_test_django
```

### 2. Copia y edita el archivo de variables de entorno

```bash
cp .env.example .env
```

- Genera un valor seguro para `DJANGO_SECRET_KEY`:

```bash
openssl rand -base64 32
```

- Pega ese valor en la línea `DJANGO_SECRET_KEY=` de tu `.env`
- Asegúrate de que el resto de valores quede así:

```env
DJANGO_DEBUG=True
POSTGRES_DB=tech_test_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
```

### 3. Construye las imágenes Docker

Se puede ejecutar alguno de los dos comandos:

```bash
make build 
docker compose build
```

### 4. Levanta los servicios

Se puede ejecutar alguno de los dos comandos:
```bash
make up
docker compose up -d
```

Esto arrancará:
- db (PostgreSQL) con volumen persistente
- web (Django + Gunicorn), aplicará migraciones, creará el superusuario y recogerá archivos estáticos.

### 5. Verifica que todo esté funcionando

```bash
docker compose ps
```

Debes ver los contenedores `db` y `web` en estado `Up`.

### 6. Accede al panel de administración de Django

Visita: [http://localhost:8000/admin/](http://localhost:8000/admin/)

- Usuario: `admin`
- Contraseña: `admin`

## 📫 Endpoints disponibles

Una vez levantado, puedes acceder a los endpoints en:

- Lista de usuarios: `GET /api/usuarios/`
- Crear usuario: `POST /api/usuarios/`
- Editar usuario: `PUT /api/usuarios/<id>/`
- Eliminar usuario: `DELETE /api/usuarios/</id>/`
- Lista de ingresos: `GET /api/ingresos/`
- Crear ingreso: `POST /api/ingresos/`

Usa Thunder Client, Postman o cualquier herramienta para hacer pruebas.

### Ejemplo de payload para crear un usuario

```json
{
  "first_name": "Juan",
  "last_name": "Perez",
  "email": "juan@example.com", 
}
```

### Ejemplo de payload para crear un ingreso

```json
{
  "fecha_entrada": "2024-07-01T08:00:00Z",
  "fecha_salida": "2024-07-01T17:00:00Z",
  "usuario": 1
}
```

**Nota**: Asegúrate de usar un ID de usuario válido al momento de crear un ingreso.

## Autor

Desarrollado por Daniela Ducuara
