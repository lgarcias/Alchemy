# Modelos de la Base de Datos

## Character
Representa un personaje en el juego.

- **id**: Identificador único.
- **name**: Nombre del personaje.
- **character_class**: Clase del personaje (e.g., Alchemist, Warrior).
- **stats**: Estadísticas del personaje (JSON).
- **abilities**: Lista de habilidades del personaje (JSON).
- **user_id**: Identificador del usuario propietario (opcional).

## BaseCharacter
Clase base para plantillas de personajes.

- **character_class**: Nombre de la clase del personaje.

## Alchemist
Hereda de `BaseCharacter`.

- **stats**: Estadísticas específicas para la clase Alchemist.
- **abilities**: Habilidades específicas para la clase Alchemist.

## Warrior
Hereda de `BaseCharacter`.

- **stats**: Estadísticas específicas para la clase Warrior.
- **abilities**: Habilidades específicas para la clase Warrior.

[Volver al README](../README.md)
