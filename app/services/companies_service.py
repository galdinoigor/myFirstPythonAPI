from sqlalchemy.orm import Session

def get_companies_by_person(db: Session, person_id: int):
    query = """
    select distinct 
    person_id, 
    company_name 
    from shared_drive.people
    WHERE person_id = :person_id
    """
    result = db.execute(query, {"person_id": person_id}).fetchall()
    if result:
        return [{"person_id": row.person_id, "company_name": row.company_name} for row in result]
    return []