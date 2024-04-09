from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Ft9ZxD87@localhost/fast_api_study"

engine = create_engine(SQLALCHEMY_DATABASE_URL, client_encoding='utf8')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

conn = engine.connect()
print(conn.get_isolation_level())