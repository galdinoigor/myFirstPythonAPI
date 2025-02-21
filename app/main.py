# Importando rotas
from app.routes.funding_by_person import router as funding_router
from app.routes.companies_by_person import router as companies_router
from app.routes.investors_by_company import router as investors_router

from fastapi import FastAPI

# Criacao da instancia da API
app = FastAPI()

# Registrar as rotas
app.include_router(funding_router)
app.include_router(companies_router)
app.include_router(investors_router)

if __name__ == "__main__":
    # inicia servidor web, habilitando acesso via HTTP
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
