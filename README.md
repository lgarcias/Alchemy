# Rogue Alchemy

Proyecto estructurado para MVP Dungeon Exploration y sistema de alquimia/deckbuilding.

- Backend: FastAPI + PostgreSQL
- Frontend: Godot 4.2+

Ver `/docs` para detalles de diseño y tareas.

---

## Instalación y configuración del entorno de desarrollo y testing

### 1. Requisitos previos
- Docker y Docker Compose
- VS Code (recomendado) con la extensión Dev Containers

### 2. Variables de entorno
- Copia el archivo `.env.example` a `.env` y ajusta los valores si es necesario.

### 3. Arrancar el entorno de desarrollo
Desde la raíz del proyecto:
```bash
docker compose up --build
```
O abre el proyecto en VS Code y usa "Reopen in Container".

### 4. Instalación automática de dependencias
Al crear o reconstruir el contenedor, se ejecuta automáticamente el script `backend/scripts/setup_venv.sh` que:
- Crea el entorno virtual `.venv` en `/workspace/backend`
- Instala todas las dependencias de desarrollo y test

### 5. Ejecutar los tests
Puedes ejecutar los tests de backend de varias formas:
- Desde VS Code: `Ctrl+Shift+P` → "Run Task" → "Run Backend Tests"
- Desde terminal en el contenedor:
  ```bash
  cd backend
  .venv/bin/python -m pytest --maxfail=3 --disable-warnings -v
  ```

### 6. Notas
- La base de datos de test se crea automáticamente si no existe.
- Las variables de entorno se cargan desde `.env`.
- No es necesario montar `.venv` como volumen: se recrea automáticamente tras cada rebuild.

---

## Documentación
- [Modelos de la Base de Datos](docs/database_models.md)
- [Endpoints Disponibles](docs/api_endpoints.md)

Para cualquier duda, consulta los archivos de ejemplo o el script de setup.
