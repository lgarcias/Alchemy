import os
import sys

# Asegurar que el directorio actual esté en PYTHONPATH
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from database import engine
from models.character import Character
from models import Base

# Asegurar que el script de creación de tablas utilice la base de datos de prueba definida en .env
os.environ['POSTGRES_DB'] = os.getenv('POSTGRES_DB_TEST', 'alchemydb_test')

# Crear todas las tablas definidas en los modelos
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas correctamente.")
