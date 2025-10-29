from fastapi import FastAPI
from app.routes import user_routes
from app.core.database import Base, engine

# Cria as tabelas (somente na primeira execução)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="My FastAPI App")

app.include_router(user_routes.router)