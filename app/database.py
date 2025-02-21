from app.config_postgre import settings

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = settings.DATABASE_URL

# criacao da conexao com banco de dados
engine = create_engine(DATABASE_URL)

# criacao da sessao para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# fecha conexão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
