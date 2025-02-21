from app.database import get_db
from app.services.investors import get_investors_by_company

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# definindo a rota /investors-by-company
router = APIRouter(prefix="/investors-by-company", tags=["Investors", "Company"])

@router.get("/{company}")
def inestors_by_company(company: str, db: Session = Depends(get_db)):
    result = get_investors_by_company(db, person_id)
    if not result:
        raise HTTPException(status_code=404, detail="Empresa não encontrada!")
    return {"company": company, "investors": result}
