import os
import sys
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from app.main import app
from app.models.character import Base, Character
from app.database import get_db
from dotenv import load_dotenv
from app.tests.factories import CharacterFactory

# Agregar dinámicamente el directorio `backend/app` al `PYTHONPATH` para resolver problemas de importación.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../app')))

# Cargar directamente el archivo de entorno de pruebas
load_dotenv('../../.env', override=True)

# Configurar directamente la URL de la base de datos de pruebas
TEST_DATABASE_URL = (
    f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT', '5432')}/{os.getenv('POSTGRES_DB_TEST')}"
)

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    # Create tables
    Base.metadata.create_all(bind=engine)
    yield
    # Drop tables after tests
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db_session():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

@pytest.fixture(scope="function")
def client(db_session):
    # Override the get_db dependency to use the test session
    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c

# Ensure the database contains character class templates before testing
@pytest.fixture(scope="function", autouse=True)
def setup_character_classes(db_session):
    # Use Factory Boy to create character class templates
    CharacterFactory.create_batch(2, name="Alchemist Template", character_class="Alchemist")
    CharacterFactory.create_batch(2, name="Warrior Template", character_class="Warrior")
