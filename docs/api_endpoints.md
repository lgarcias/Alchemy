# Endpoints Disponibles

## POST `/api/v1/characters`
**Descripción**: Crear un nuevo personaje.

**Parámetros**:
- **name** (string): Nombre del personaje.
- **character_class** (string): Clase del personaje.
- **stats** (JSON): Estadísticas del personaje.
- **abilities** (array): Lista de habilidades del personaje.

**Ejemplo de uso**:
```bash
curl -X POST http://localhost:8000/api/v1/characters -H "Content-Type: application/json" -d '{"name": "Hero", "character_class": "Warrior", "stats": {"hp": 100, "damage": 20}, "abilities": ["Slash", "Block"]}'
```

---

## GET `/api/v1/characters`
**Descripción**: Listar todos los personajes.

**Parámetros**:
- **skip** (int, opcional): Número de registros a omitir para paginación.
- **limit** (int, opcional): Número máximo de registros a devolver.

**Ejemplo de uso**:
```bash
curl -X GET http://localhost:8000/api/v1/characters
```

---

## GET `/api/v1/characters/{character_id}`
**Descripción**: Obtener un personaje por su ID.

**Parámetros**:
- **character_id** (int): ID único del personaje.

**Ejemplo de uso**:
```bash
curl -X GET http://localhost:8000/api/v1/characters/1
```

---

## PUT `/api/v1/characters/{character_id}`
**Descripción**: Actualizar un personaje por su ID.

**Parámetros**:
- **character_id** (int): ID único del personaje.
- **name** (string): Nombre actualizado del personaje.
- **character_class** (string): Clase actualizada del personaje.
- **stats** (JSON): Estadísticas actualizadas del personaje.
- **abilities** (array): Lista de habilidades actualizadas del personaje.

**Ejemplo de uso**:
```bash
curl -X PUT http://localhost:8000/api/v1/characters/1 -H "Content-Type: application/json" -d '{"name": "Updated Hero", "character_class": "Mage", "stats": {"hp": 80, "damage": 30}, "abilities": ["Fireball", "Teleport"]}'
```

---

## DELETE `/api/v1/characters/{character_id}`
**Descripción**: Eliminar un personaje por su ID.

**Parámetros**:
- **character_id** (int): ID único del personaje.

**Ejemplo de uso**:
```bash
curl -X DELETE http://localhost:8000/api/v1/characters/1
```

[Volver al README](../README.md)
