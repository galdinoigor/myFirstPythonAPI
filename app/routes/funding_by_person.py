from app.database import get_db
from app.services.funding_service import get_avg_funding_by_person

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# definindo a rota /avg-funding-by-person
router = APIRouter(prefix="/avg-funding-by-person", tags=["Funding"])

@router.get("/{person_id}")
def avg_funding(person_id: str, db: Session = Depends(get_db)):
    result = get_avg_funding_by_person(db, person_id)
    if not result:
        return {"person_id": person_id, "average_funding": "0"}
    return {"person_id": person_id, "average_funding": result}
