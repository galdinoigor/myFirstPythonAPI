from app.database import get_db
from app.services.companies_service import get_companies_by_person

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# definindo a rota /avg-funding-by-person
router = APIRouter(prefix="/companies-by-person", tags=["Companies"])

@router.get("/{person_id}")
def companies_by_person(person_id: int, db: Session = Depends(get_db)):
    result = get_companies_by_person(db, person_id)
    if not result:
        raise HTTPException(status_code=404, detail="person_id inválido ou não há empresas cadastradas para este person_id.")
    return {"person_id": person_id, "companies": result}